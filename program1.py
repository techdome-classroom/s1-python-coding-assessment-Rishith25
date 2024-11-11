class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here  
        if not grid:
            return 0
        
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'W':
                return
            grid[x][y] = 'W'
            
            dfs(x + 1, y)  
            dfs(x - 1, y)  
            dfs(x, y + 1)  
            dfs(x, y - 1) 
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    dfs(i, j)
                    count += 1
        
        return count
                    
