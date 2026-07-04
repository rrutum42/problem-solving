class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top, bot = 0 , rows -1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break



        l,r = 0, cols -1 

        while l<=r:
            mid = (l+r)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] <= target:
                l = mid + 1
            else:
                r = mid -1
        return False

                    