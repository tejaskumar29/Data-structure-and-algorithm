class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        
        min_val = min(nums)
        max_val = max(nums)
        
        missing = []
        
        # Step 2: Check every number between min and max
        for i in range(min_val + 1, max_val):
            if i not in num_set:
                missing.append(i)
                
        # Step 3: Return the sorted missing elements
        return missing