# O(1) space complexity
class Solution:
    def gameOfLife(self, board):
        def countNeighbor(r, c, board):
            DIR = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
            count = 0
            for dc, dr in DIR:
                nc = c + dc
                nr = r + dr
                if nc >= 0 and nr >= 0 and nc < len(board[0]) and nr < len(board):
                    count += board[nr][nc]
            return count
                
        
        new_state = [[-1] * len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    if countNeighbor(row, col, board) == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0
                else:
                    if countNeighbor(row, col, board) < 2 or countNeighbor(row, col, board) > 3:
                        new_state[row][col] = 0
                    else:
                        new_state[row][col] = 1
        print(new_state)
        board = new_state

# No extra space

class Solution:
    def gameOfLife(self, board):
        def countNeighbor(r, c, board):
            DIR = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
            count = 0
            for dc, dr in DIR:
                nc = c + dc
                nr = r + dr
                if nc >= 0 and nr >= 0 and nc < len(board[0]) and nr < len(board):
                    if board[nr][nc] == 2:
                        count += 0
                    elif board[nr][nc] == -1:
                        count += 1
                    else:
                        count += board[nr][nc]
            return count
                
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    if countNeighbor(row, col, board) == 3:
                        board[row][col] = 2
                    else:
                        board[row][col] = 0
                else:
                    if countNeighbor(row, col, board) < 2 or countNeighbor(row, col, board) > 3:
                        board[row][col] = -1
                    else:
                        board[row][col] = 1
                        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == -1:
                    board[r][c] = 0 
                elif board[r][c] == 2:
                    board[r][c] = 1


