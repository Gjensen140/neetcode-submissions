class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        l = 0
        r = n - 1
        
        max_left = height[l]
        max_right = height[r]
        output = 0

        while l <= r:
            h = min(max_left, max_right)
            
            if height[l] <= height[r]:
                diff = h - height[l]
                
                if diff > 0:
                    output += diff
                
                l += 1

                if l < n:
                    max_left = max(max_left, height[l])
            else:
                diff = h - height[r]
                
                if diff > 0:
                    output += diff
                
                r -= 1

                if r > 0:
                    max_right = max(max_right, height[r])

        return output
