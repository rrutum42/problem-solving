class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force 
        # for each row check validity (contains duplicate)
        # for each column check validity (contains duplicate)
        # for each grid check validity 

        # one pass solution:
        # for each row and column ad box check if element 
        # O(81) -> O(1)
        # O(81*3) -> O(243) -> O(1)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        return True