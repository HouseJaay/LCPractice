class Solution:
    def islandPerimeter(self,grid):
        count_line = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])-1):
                if grid[j][i] and grid[j][i+1]:
                    count_line += 1
        for i in range(len(grid[0])):
            for j in range(len(grid)-1):
                if grid[j][i] and grid[j+1][i]:
                    count_line += 1
        count_land = sum(map(sum,grid))
        return count_land*4 - count_line*2
