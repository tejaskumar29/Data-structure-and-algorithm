# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
         # Search between version 1 and version n
        left, right = 1, n

        # Continue until both pointers meet
        while left < right:

            # Find the middle version
            mid = (left + right) // 2

            # If mid is bad,
            # the first bad version could be mid or before it
            if isBadVersion(mid):
                right = mid

            # If mid is good,
            # the first bad version must be after mid
            else:
                left = mid + 1

        # Both pointers point to the first bad version
        return left