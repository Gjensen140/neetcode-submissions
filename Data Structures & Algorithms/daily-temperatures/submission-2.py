class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Output array
        n = len(temperatures)
        output = [0] * n

        # Tracking the temps that need to be updated
        stack = []
        cur = 0

        while cur < n:
            
            while (len(stack) > 0) and (temperatures[cur] > stack[-1][0]):
                out = stack.pop()
                output[out[1]] = cur - out[1] 
            # Storing index-value pairs
            val = [temperatures[cur], cur]
            stack.append(val)
            
            cur += 1
        
        return output
