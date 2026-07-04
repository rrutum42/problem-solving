class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []

        pac,atl = set(),set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,visited,prevHeight):
            if(
                r<0 or c<0 or
                r>=rows or c>=cols or
                heights[r][c] < prevHeight or 
                (r,c) in visited
            ):
                return
            
            visited.add((r,c))
            currHeight = heights[r][c]
            dfs(r+1,c,visited,currHeight)
            dfs(r-1,c,visited,currHeight)
            dfs(r,c+1,visited,currHeight)
            dfs(r,c-1,visited,currHeight)

        for r in range(rows):
            # first col for pacific
            dfs(r,0,pac,heights[r][0])
            # last col for atlantic
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        
        return ans
        