import queue
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    
        DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        def bfs(start_y, start_x):
            q = queue.Queue()
            q.put((start_y, start_x))
            grid[start_y][start_x] = "0"
  
            while not q.empty():
                y, x = q.get()
                for dy, dx in DIR:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x >= 0 and new_x < len(grid[0]) and new_y >= 0 and new_y < len(grid):
                        if grid[new_y][new_x] == "1":
                            q.put((new_y, new_x))
                            grid[new_y][new_x] = "0"
        
        num_island = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    bfs(y, x)
                    num_island += 1
        return num_island
        
