class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        lowest = l
        while l<=r:
            m = (l+r)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/m)

            if totalTime <= h:
                r = m - 1
                lowest = m
            else:
                l = m + 1
        return lowest
            