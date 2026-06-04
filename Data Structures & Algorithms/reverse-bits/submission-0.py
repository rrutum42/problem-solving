class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32):
            bit = n>>i&1
            res += (bit << (31-i))
        return res


'''
Read the ith bit and if 1 set the 31-i bit of res
'''