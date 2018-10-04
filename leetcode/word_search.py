# https://leetcode.com/problems/word-search/description/

# RECURSION APPROACH:
class Solution:
    def __init__(self):
        self.cur_index = 0
        
    def exist(self, board, word):
        DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def find_start(board, word):
            possible_starts = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        possible_starts.append((i, j)) 
            return possible_starts
                    
        
        def dfs(start_y, start_x):
            visited[start_y][start_x] = True
            self.cur_index += 1
            if self.cur_index == len(word):
                return True
            for dy, dx in DIR:
                new_y = start_y + dy
                new_x = start_x + dx
                if new_y >= 0 and new_x >= 0 and new_y < len(board) and new_x < len(board[0]):
                    if not visited[new_y][new_x] and board[new_y][new_x] == word[self.cur_index]:

                        if dfs(new_y, new_x):
                            return True
            self.cur_index -= 1
            visited[start_y][start_x] = False
            return False
        
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        possible_starts = find_start(board, word)
        for start_y, start_x in possible_starts:
            if dfs(start_y, start_x):
                print(self.cur_index)
                return True
        return False

# ITERATIVE APPROACH:
       class Solution:
        
    def exist(self, board, word):
        DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        def find_start(board, word):
            possible_starts = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        possible_starts.append((i, j)) 
            return possible_starts
                    
        # Store a node in the form of (y, x, cur_index, backtrack)
        def dfs(start_y, start_x):
            visited = [[False] * len(board[0]) for _ in range(len(board))]
            stack = []
            stack.append((start_y, start_x, 0, False))
            visited[start_y][start_x] = True
            
            while stack:
                y, x, cur_index, backtrack = stack.pop()
                if backtrack:
                    visited[y][x] = False
                    continue
                visited[y][x] = True
                stack.append((y, x, cur_index, True)) # Add backtracking node
                
                if cur_index == len(word) - 1:
                    return True
                
                for dy, dx in DIR:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_x >= 0 and new_y < len(board) and new_x < len(board[0]):
                        if not visited[new_y][new_x]:
                            if board[new_y][new_x] == word[cur_index + 1]:
                                stack.append((new_y, new_x, cur_index + 1, False)) # Add moving-forward node
                
            
        
        possible_starts = find_start(board, word)
        for start_y, start_x in possible_starts:
            if dfs(start_y, start_x):
                return True
        return False
       
