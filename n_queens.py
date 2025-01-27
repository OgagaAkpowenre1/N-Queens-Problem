import streamlit as st
import numpy as np

def solve_n_queens(n):
    board = np.zeros((n, n), dtype=int)
    solutions = []

    def is_safe(board, row, col):
        # Check the column and diagonals
        for i in range(row):
            if board[i, col] == 1:  # Check the column
                return False
            if col - (row - i) >= 0 and board[i, col - (row - i)] == 1:  # Check the left diagonal
                return False
            if col + (row - i) < n and board[i, col + (row - i)] == 1:  # Check the right diagonal
                return False
        return True

    def backtrack(board, row):
        if row == n:
            solutions.append(board.copy())
            return True

        for col in range(n):
            if is_safe(board, row, col):
                board[row, col] = 1
                if backtrack(board, row + 1):
                    return True
                board[row, col] = 0
        return False

    backtrack(board, 0)
    return solutions

st.header('N-Queens Problem')

st.write("This is a visualization of the N-Queens problem. 1's represent Queens and 0's empty space.")

n = st.slider("Select N (size of board)", 4, 10, 8)
solutions = solve_n_queens(n)

st.write(f"Solutions for {n}-Queens Problem:")
for solution in solutions:
    st.write(solution)
