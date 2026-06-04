class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            ia = a>>i & 1
            ib = b>>i & 1
            cur_bit = ia ^ ib ^ carry
            carry = (ia + ib + carry) >= 2
            if cur_bit:
                res += (1<<i)
        if res & (1 << 31):  # if the 32nd bit is set (sign bit)
            res = res - (1 << 32) # subtract 2^32 to convert to negative range

        return res

        