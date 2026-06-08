class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.desc = nums
        heapq.heapify(self.desc)
        while len(self.desc) > k:
            heapq.heappop(self.desc)

    def add(self, val: int) -> int:
        heapq.heappush(self.desc, val)
        if len(self.desc) > self.k:
            heapq.heappop(self.desc)
        return self.desc[0]

'''
Time complexity: 
O(m∗logk)
Space complexity: 
O(k)
'''
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)