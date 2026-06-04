class MedianFinder:

    def __init__(self):
        '''
        small heap contains the max heap
        large heap contains the min heap
        '''
        self.small, self.large = [], []
                
    def addNum(self, num: int) -> None:
        '''
        always push to the small heap
        make sure every element in small <= every el in large
            if not smaller then move to large heap
        if small > large + 1
            remove from large and put in small
        if large > small + 1
            remove from large and put in small
        '''
        # heapq.heappush(self.small, -1*num)

        # if (
        #     self.small and self.large and 
        #     (-1 * self.small[0]) > self.large[0] 
        # ):
        #     val = -1 * heapq.heappop(self.small)
        #     heapq.heappush(self.large, val)
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small)> len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large)> len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        '''
        find the max of small heap O(1)
        find the min of large heap O(1)
        if number of elements is odd 
        then return the max of small and min of large heap
        '''
        if len(self.small)> len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0]+self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()