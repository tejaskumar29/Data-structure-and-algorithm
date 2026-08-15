class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = 0

        while low <= high:
            mid = low + (high - low) // 2

            if self.calculateHours(piles, mid) <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

    def calculateHours(self, piles, k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours