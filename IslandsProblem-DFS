class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        #define the dfs search so it can work recursively
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs (row, col - 1)
        
        #iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands


        
        
