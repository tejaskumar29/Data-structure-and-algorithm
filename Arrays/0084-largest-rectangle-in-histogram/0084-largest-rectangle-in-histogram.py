class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # keeps indices of bars, heights always increasing
        max_area = 0
        heights = heights + [0]   # sentinel: forces everything left to pop at the end

        for i, h in enumerate(heights):
        # current bar is shorter than the one on top of the stack?
        # that top bar can't stretch any further right -> pop and measure it
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area