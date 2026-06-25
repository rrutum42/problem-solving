class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs
        og_color = image[sr][sc]
        def dfs(r,c):
            if (r<0 or c<0 or r>=len(image) or c>=len(image[0])
            or image[r][c] != og_color):
                return
            curr_color = image[r][c]
            
            image[r][c] = color
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        if og_color == color:
            return image
        dfs(sr,sc)
        return image