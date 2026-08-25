class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Add to 'ones', but remove it if it's already in 'twos'
            ones = (ones ^ num) & ~twos
            # Add to 'twos', but remove it if it's already in 'ones'
            twos = (twos ^ num) & ~ones
            
        # When everything is processed, the single number is trapped in 'ones'
        return ones