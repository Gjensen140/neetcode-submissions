class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        l = 0
        r = n - 1

        output = -1

        while l < r:
            h1 = heights[l]
            h2 = heights[r]

            area = (r - l) * min(h1, h2)

            output = max(output, area)

            if h1 < h2:
                l += 1
            else:
                r -= 1

        return output