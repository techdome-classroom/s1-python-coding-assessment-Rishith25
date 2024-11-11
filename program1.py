class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here  
        if not grid:
            return 0
        
        def dfs(x, y):
            # Check boundaries and ensure the cell is land
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'W':
                return
            # Mark the current cell as visited by setting it to 'W'
            grid[x][y] = 'W'
            
            # Explore all four directions
            dfs(x + 1, y)  # down
            dfs(x - 1, y)  # up
            dfs(x, y + 1)  # right
            dfs(x, y - 1)  # left
        
        island_count = 0
        
        # Traverse every cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If cell is land, it's a new island
                if grid[i][j] == 'L':
                    dfs(i, j)
                    island_count += 1
        
    return island_count
                    
