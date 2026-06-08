class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0 
        area = 0 
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c) -> int:
            if (
                r<0 or c<0 or
                r>=rows or c>=cols or
                grid[r][c] == 0
            ):
                return 0
        
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                islandArea = dfs(r,c)
                area = max(area,islandArea)
        
        return area

        