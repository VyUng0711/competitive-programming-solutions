# https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def addsolution():
            this_solution = []
            for i in range(n):
                this_row = ""
                for j in range(n):
                    if board[i][j]:
                        this_row += "Q"
                    else:
                        this_row += "."
                this_solution.append(this_row)
            solution.append(this_solution)
        def check(board, row, col):
            # Check the column
            for i in range(row):
                if board[i][col]:
                    return False
            # Check the two diagonals (only the upper part):
            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1
            i = row
            j = col
            while j < n and i >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j += 1
            return True
        
        def nqueen(board, row):
            if row == n:
                # printsolution()
                addsolution()
                # print()
                return True
            for j in range(n):
                if check(board, row, j) == True:
                    board[row][j] = 1
                    nqueen(board, row + 1)
                    board[row][j] = 0
            return False
        
        board = [[0] * n for _ in range(n)]
        solution = []
        nqueen(board, 0)
        return solution

