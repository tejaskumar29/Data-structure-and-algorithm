class Solution:
    def getSum(self, a: int, b: int) -> int:
        arr=[]
        arr.append(a)
        arr.append(b)
        return sum(arr)

        # mask = 0xFFFFFFFF  # 32 bit mask
        # maxInt = 2**31 - 1

        # while b != 0:
        #     sum = (a ^ b) & mask # contain to 32 bits
        #     carry = (a & b) & mask # contain to 32 bits
        #     a = sum
        #     b = carry << 1
        
        # return a if a <= maxInt else ~(a ^ mask)