class Solution:
    # O(m*n), O(m*n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c):
            if(
                r<0 or c<0 or
                r==ROWS or c==COLS or
                board[r][c] != "O" 
            ):
                return
            
            board[r][c] = "#"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # check first and last column
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)

        # check first and last row
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

'''
capture anything which is surrounded by x 
check first row fir col and last row last column for reachable 0
if reachable then dont surround them
'''