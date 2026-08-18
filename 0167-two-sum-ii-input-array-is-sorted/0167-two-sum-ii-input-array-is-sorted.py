class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        h=n-1
        while l<h:
            sumi=numbers[l]+numbers[h]
            if sumi==target:
                return [l+1,h+1]
            elif sumi<target:
                l+=1
            else:
                h-=1
        return []
            
        