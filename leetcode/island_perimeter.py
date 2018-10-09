# https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid):
        count = 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for dx, dy in DIR:
                        nx = j + dx
                        ny = i + dy
                        if nx < 0 or ny < 0 or nx > len(grid[0]) - 1 or ny > len(grid) - 1:
                            count += 1
                        else:
                            if grid[ny][nx] == 0:
                                count += 1
                    # print(count)
        return count

