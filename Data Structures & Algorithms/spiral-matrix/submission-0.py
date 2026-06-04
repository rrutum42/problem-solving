class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        l,r = 0, n-1
        top,bottom = 0, m-1

        ans = []

        while l<=r and top<=bottom:
            # cover the top row from left to right
            for i in range(l,r+1):
                ans.append(matrix[top][i])
            # move top to next row
            top += 1

            # cover the last column from top to bottom
            for i in range(top, bottom+1):
                ans.append(matrix[i][r])
            # move the right row inwards
            r -= 1

            # check if there is even a row left to print
            if top <= bottom:
                # cover the last row from right to left
                for i in range(r,l-1,-1):
                    ans.append(matrix[bottom][i])
                # move bottom to upper row
                bottom -= 1

            # check if there is even a column left to print
            if l <= r:
                # cover the first column from bottom to top
                for i in range(bottom, top -1,-1):
                    ans.append(matrix[i][l])
                # move the left to next column
                l += 1
        
        return ans

        