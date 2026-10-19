class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0
        seen = set()
        output = 0

        for r in range(n):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            diff = r - l + 1
            output = max(output, diff)

        return output