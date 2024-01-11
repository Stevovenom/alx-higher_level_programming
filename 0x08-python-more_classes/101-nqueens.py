#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (list): The N x N chessboard represented as a 2D list.
        row (int): The row index.
        col (int): The column index.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen at position (row, col), False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    A recursive function to solve the N-Queens problem using backtracking.

    Args:
        board (list): The N x N chessboard represented as a 2D list.
        col (int): The current column index.
        N (int): The size of the chessboard.
        solutions (list): A list to store the solutions found.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0  # backtrack if placing queen at board[i][col] doesn't lead to a solution

    return res


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all solutions.

    Args:
        N (int): The size of the chessboard.

    Returns:
        int: 0 if successful, 1 if there's an error.
    """
    if not isinstance(N, int):
        print("N must be a number")
        return 1
    if N < 4:
        print("N must be at least 4")
        return 1

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
