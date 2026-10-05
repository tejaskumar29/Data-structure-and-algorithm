class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
    
    # 1. Divide the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
    
    # 2. Conquer: Merge the sorted halves
        return self.merge(left_half, right_half)

    def merge(self,left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
    
    # Compare elements from both halves and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
    # Append any remaining elements from either half
        result.extend(left[i:])
        result.extend(right[j:])
    
        return result