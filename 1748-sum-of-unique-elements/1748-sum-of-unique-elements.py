class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq_nums=Counter(nums)
        s=0
        for k,v in freq_nums.items():
            if v==1:
                s=s+k
        return s       