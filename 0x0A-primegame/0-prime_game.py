#!/usr/bin/python3


def isWinner(x, nums):
    def sieve(n):
        primes = []
        sieve = [True] * (n+1)
        for p in range(2, n+1):
            if sieve[p]:
                primes.append(p)
                for i in range(p*p, n+1, p):
                    sieve[i] = False
        return primes

    def can_win(n, primes):
        if n == 1:
            return False
        if n in primes:
            return True
        for p in primes:
            if n % p == 0:
                return False
        return True

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        primes = sieve(n)
        maria_turn = True
        while n > 1:
            if maria_turn:
                for p in primes:
                    if n % p == 0:
                        n -= p
                        break
                else:
                    n -= 1
            else:
                for p in primes:
                    if n % p == 0:
                        n -= p
                        break
                else:
                    n -= 1
            maria_turn = not maria_turn
        if maria_turn:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None
