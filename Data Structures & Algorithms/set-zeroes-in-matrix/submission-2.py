class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC O(2 m*n) SC O(1)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # instead of storing which rows to make 0, just mark the start of the row/col as 0 and on second iter marks all elems in the row/col as 0 
        # zeroCol = 1
        rowZero = False
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0 :
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
                    # # mark the ith row 
                    # matrix[i][0] = 0
                    # # mark the column except 1st column
                    # if j > 0:
                    #     matrix[0][j] = 0
                    # else:
                    #     zeroCol = 0

        # change all excpet 1st row and col
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # change the rows first
        if matrix[0][0] == 0:
            for j in range(ROWS):
                matrix[j][0] = 0
        
        # change the col 
        # if zeroCol == 0:
        #     for i in range(COLS):
        #         matrix[0][i] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        # # TC O(2 m*n) SC O(m+n)
        # m = len(matrix)
        # n = len(matrix[0])
        # rows = set()
        # cols = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0 :
        #             rows.add(i)
        #             cols.add(j)

        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0