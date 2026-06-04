class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)

        bucket = [[] for i in range (len(nums)+1)]       
        for n,cnt in count.items():
            bucket[cnt].append(n)

        res=[]
        l = len(bucket) - 1
        for i in range(l):
            for num in bucket[l-i]:
                res.append(num)
                if len(res) == k:
                    return res

