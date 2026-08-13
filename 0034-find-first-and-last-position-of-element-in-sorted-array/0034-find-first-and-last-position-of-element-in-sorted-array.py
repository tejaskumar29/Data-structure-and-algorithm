class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, is_searching_left):
            left, right = 0, len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    # We found the target! Save it, but keep looking.
                    idx = mid
                    if is_searching_left:
                        right = mid - 1  # Look towards the left for the start
                    else:
                        left = mid + 1   # Look towards the right for the end
                        
            return idx

        # Run binary search twice
        start = binarySearch(nums, target, True)
        end = binarySearch(nums, target, False)
        
        return [start, end]