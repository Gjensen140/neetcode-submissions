# Idea: Track a left and right, continually move inward until area is maximized

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            area = h * (r - l)
            if area > output:
                output = area
            
            # Adjusting inwards: Always move the smaller of the two
            if heights[l] == h:
                l += 1
            else:
                r -= 1
        
        return output

