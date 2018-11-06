# https://leetcode.com/problems/design-tic-tac-toe/
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        # self.grid = [[0] * n for _ in range(n)]
        self.n = n
        self.vertical = {}
        self.len_vertical = {k: 0 for k in range(n)}
        self.horizontal = {}
        self.len_horizontal = {k: 0 for k in range(n)}
        self.right_dia = 0
        self.len_right_dia = 0
        self.left_dia = 0 
        self.len_left_dia = 0
                    

    def move(self, row, col, player):
        # self.grid[row][col] = player
        if col not in self.vertical:
            self.vertical[col] = player
            self.len_vertical[col] += 1
            if self.len_vertical[col] == self.n:
                return player
        else:
            if self.vertical[col] == player:
                self.len_vertical[col] += 1
                if self.len_vertical[col] == self.n:
                    return player
            else:
                self.vertical[col] = None
            
        if row not in self.horizontal:
            self.horizontal[row] = player
            self.len_horizontal[row] += 1
            if self.len_horizontal[row] == self.n:
                return player
        else:
            if self.horizontal[row] == player:
                self.len_horizontal[row] += 1
                if self.len_horizontal[row] == self.n:
                    return player
            else:
                self.horizontal[row] = None
                
        if row == col:
            if self.right_dia != None:
                if self.right_dia == 0:
                    self.right_dia = player
                    self.len_right_dia += 1
                else:
                    if self.right_dia != player:
                        self.right_dia = None
                    else:
                        self.len_right_dia += 1
                        if self.len_right_dia == self.n:
                            return player
            
        
        if row + col == self.n - 1:
            if self.left_dia != None:
                if self.left_dia == 0:
                    self.left_dia = player
                    self.len_left_dia += 1
                else:
                    if self.left_dia != player:
                        self.left_dia = None
                    else:
                        self.len_left_dia += 1
                        if self.len_left_dia == self.n:
                            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# Shorter solution:
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.vertical = [0] * n
        self.horizontal = [0] * n
        self.right_dia = 0
        self.left_dia = 0 
                    
    def move(self, row, col, player):
        if player == 1:
            score = -1
        else:
            score = 1
            
        self.vertical[col] += score
        if self.vertical[col] == self.n or self.vertical[col] == -self.n:
            return player
        self.horizontal[row] += score
        if self.horizontal[row] == self.n or self.horizontal[row] == -self.n:
            return player
        
        if row == col:
            self.right_dia += score
            if self.right_dia == self.n or self.right_dia == -self.n:
                return player
        
        if row + col == self.n - 1:
            self.left_dia += score
            if self.left_dia == self.n or self.left_dia == -self.n:
                return player
            
        return 0
