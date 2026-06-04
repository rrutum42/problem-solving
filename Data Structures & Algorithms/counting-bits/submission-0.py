class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1, n+1):
            n = i
            while n != 0:
                n = n & (n-1)
                ans[i] += 1
        return ans