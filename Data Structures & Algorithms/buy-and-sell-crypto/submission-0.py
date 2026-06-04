class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ln = len(prices)

        if ln == 1:
            return 0
        
        maxp = 0
        l,r = 0, 1

        while r<ln:
            # if buy > sell then move right
            if prices[l] > prices[r]:
                l += 1
            else:
                maxp = max(maxp,(prices[r]-prices[l]))
                r += 1 
        return maxp
 
'''
find the index of the minimum profit 

min(p)
 
find the maximum to the right of the min(p) index 

subtract

max profit = 0
while l < r:
    maxp = max(maxp,(p[r]-p[l]))
    r += 1

iterate i over entire array
check for the smallest value to the left of i
that is the max profit if we sell on ith day
move i forward, check same for each 

7 1 5 3 6 4

between any two numbers, total profit/loss
 = p[i] 
6,7 = -1 = 6 -3-5-1-7
p i. -6
-2 4   i
'''        