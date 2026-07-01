class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sn=set(nums1)
        res=[]
        for elem in nums2:
            if elem in sn:
                res.append(elem)
                sn.remove(elem)
        return res