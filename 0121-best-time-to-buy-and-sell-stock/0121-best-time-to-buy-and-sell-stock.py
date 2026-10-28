class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=prices[0]
        res=0
        for i in range(1,len(prices)):
	        minsofar=min(minsofar,prices[i])
	        res=max(res,prices[i]-minsofar)
        return res