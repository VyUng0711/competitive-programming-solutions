# https://leetcode.com/problems/max-area-of-island/description/

import queue
class Solution:
    def maxAreaOfIsland(self, grid):
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(sy, sx):
            q = queue.Queue()
            q.put((sy, sx))
            grid[sy][sx] = 0
            this_size = 1
            while not q.empty():
                y, x = q.get()
                for dy, dx in DIR:
                    ny = y + dy
                    nx = x + dx
                    if nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
                        if grid[ny][nx] == 1:
                            this_size += 1
                            grid[ny][nx] = 0
                            q.put((ny, nx))
                    # print(grid, this_size)
            return this_size
        
        
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = bfs(i, j)
                    max_size = max(size, max_size)
                    
        return max_size
                    
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """

