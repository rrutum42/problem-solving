class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            # if r or c go out of bound OR
            # the letter present on the board is not equal to the letter of the word
            # or if r and c have already been visited
            if (r<0 or c<0 or r>=ROWS or c>=COLS or
                (word[i] != board[r][c]) or (r,c) in visited
            ):
                return False
            
            visited.add((r,c))
            # check dfs for all neighbouring nodes for the next letter
            res = (
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )
            visited.remove((r,c))
            return res
        
        # do a dfs for every letter on board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): 
                    return True
        return False
        