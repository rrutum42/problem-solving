class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap O(n*logk), O(k)
        dist = []
        for pt in points:
            x,y = pt[0],pt[1]
            d = -(x**2 + y**2)
            heapq.heappush(dist, [d,x,y])
            if len(dist) > k:
                heapq.heappop(dist)

        res = []
        while dist:
            d,x,y = heapq.heappop(dist)
            res.append([x,y])
        
        return res
        # # min heap O(n*logn + k*logn), O(n)
        # dist = []

        # ox,oy = 0,0
        # for pt in points:
        #     x,y = pt[0],pt[1]
        #     d = x**2 + y**2
        #     dist.append([d,x,y])

        # # print(dist)

        # heapq.heapify(dist)
        # res = []
        # while k>0:
        #     d,x,y = heapq.heappop(dist)
        #     res.append([x,y])
        #     k -= 1
        
        # return res
