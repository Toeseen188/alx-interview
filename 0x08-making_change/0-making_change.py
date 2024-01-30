#!/usr/bin/python3
"""
This dynamic programming solution uses an array dp to store the
minimum number of coins needed to make change for each amount
from 0 to total. The outer loop iterates over each coin, and
the inner loop updates the dp array based on the current coin's value.
The final result is stored in dp[total],
or -1 if it's still initialized as float('inf').
"""


def makeChange(coins, total):
    """
    function to implement make change
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
