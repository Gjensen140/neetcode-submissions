class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n <= 1:
            return n
        
        l = 0
        r = 1
        output = 0
        seen = set()
        seen.add(s[l])

        while r < n:
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            width = r - l + 1
            output = max(output, width)
            
            r += 1
            
        return output