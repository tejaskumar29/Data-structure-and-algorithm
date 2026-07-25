class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=max(candies):

                arr.append(True)
            else:
                arr.append(False)
        return arr