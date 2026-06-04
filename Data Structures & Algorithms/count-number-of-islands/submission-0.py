class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(i,j):
            if (
                i<0 or j<0 or i>=m or j>=n
                or
                grid[i][j] == "0"
            ):
                return

            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        return islands
'''
find out the number of graphs/trees?

bfs/dfs and store visited set((i,j)) 
for each node you check if it is already in visited 
not visited then add to visited and set as 0


'''      