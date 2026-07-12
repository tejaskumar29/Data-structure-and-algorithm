class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        lo=0
        mid=0
        hi=n-1
        while mid<=hi:
            if nums[mid]==0:
                nums[lo],nums[mid]=nums[mid],nums[lo]
                lo=lo+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            else:
                nums[hi],nums[mid]=nums[mid],nums[hi]
                hi=hi-1
        return nums