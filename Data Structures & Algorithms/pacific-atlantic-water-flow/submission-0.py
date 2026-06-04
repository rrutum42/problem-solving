class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prevHeight):
            if (
                r<0 or c<0 or r>=ROWS or c>=COLS or
                heights[r][c] < prevHeight or
                (r,c) in visit
            ):
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            # check the set for first row i.e. pacific
            dfs(0,c, pac, heights[0][c])
            # check the set for last row i.e. atlantic
            dfs(ROWS-1,c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
'''
instead of checking for each node if water is reachable,
we check all the reachable nodes from water
i.e. we check for all nodes adjacent to the water
pac -> first row and first column
atl -> last row and last column
maintain 2 sets, pac and atl
they contain tuple of all the coordinates of nodes that are reachable from pac and atl ocean resp

answer is a list of all the coords which are present in pac + atl

inside dfs, don't go further if the current value is less than previous value
'''