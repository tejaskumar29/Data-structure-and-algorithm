class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p = j + 1
                q = n - 1
                while p < q:
                    sum4 = nums[i] + nums[j] + nums[p] + nums[q]
                    if sum4 < target:
                        p += 1
                    elif sum4 > target:
                        q -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1
                        while p < q and nums[p] == nums[p - 1]:
                            p += 1
                        while p < q and nums[q] == nums[q + 1]:
                            q -= 1

        return ans