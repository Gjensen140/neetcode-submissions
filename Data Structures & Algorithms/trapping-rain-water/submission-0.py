class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1

        pre_max = [height[0]] * n
        post_max = [height[n-1]] * n
        
        for i in range(1, n):
            pre_max[i] = max(height[i], pre_max[i-1])

            ind = (i + 1) * -1
            post_max[ind] = max(post_max[ind + 1], height[ind])

        output = 0

        for i in range(n):
            h = min(post_max[i], pre_max[i])
            diff = h - height[i]
            if diff > 0:
                output += diff

        return output
                