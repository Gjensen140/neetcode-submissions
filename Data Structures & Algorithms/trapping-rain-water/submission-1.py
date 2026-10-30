class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        post_max = [0] * n

        pre_max[0] = height[0]
        post_max[n-1] = height[n-1]

        for i in range(1, n):
            pre_max[i] = max(height[i], pre_max[i - 1])

            post_ind = -i - 1
            post_max[post_ind] = max(post_max[-i], height[post_ind])

        output = 0

        for i in range(n):
            area = min(post_max[i], pre_max[i]) - height[i]

            if area > 0:
                output += area

        return output