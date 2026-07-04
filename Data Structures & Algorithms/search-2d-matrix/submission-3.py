class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        for i in range(rows):
            if target >= matrix[i][0]:
                row = i
        
        print(row)
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

                    