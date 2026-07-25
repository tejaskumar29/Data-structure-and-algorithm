class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if x==0:
            return 0
        if x==1:
            return 1.0
        if x==-1 and n%2==0:
            return 1.0
        if x==-1 and n%2==1:
            return -1
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result = result * current_product
            current_product = current_product * current_product
            n = n // 2
        return result