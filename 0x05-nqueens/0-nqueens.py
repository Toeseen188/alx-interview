#!/usr/bin/python3
"""
module
"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at the given position"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


def solve_n_queens(N, board, row, solutions):
    """Recursively solve the N Queens problem"""
    if row == N:
        solutions.append(list(board))
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(N, board, row + 1, solutions)


def print_solutions(N, solutions):
    """Print the solutions in a formatted way"""
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


def main():
    """Main function to parse command line arguments
    and solve the N Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * N
    solutions = []
    solve_n_queens(N, board, 0, solutions)
    print_solutions(N, solutions)


if __name__ == "__main__":
    main()
