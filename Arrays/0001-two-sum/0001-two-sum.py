class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []















        nummap={}
        n=len(nums)
        for i in range(n):
            com=target-nums[i]
            if com in nummap:
                return [nummap[com],i]
            nummap[nums[i]]=i
        return []