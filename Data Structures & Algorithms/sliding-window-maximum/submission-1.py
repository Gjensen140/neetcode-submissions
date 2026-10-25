class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        queue = collections.deque()

        l = 0
        r = 0
        output = []

        while r < n:
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if r >= k - 1:
                output.append(nums[queue[0]])
                l += 1

            r += 1



        return output
            
