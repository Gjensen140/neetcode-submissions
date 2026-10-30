class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        cur = 0
        output = 0
        counts = collections.defaultdict(int)
        l = 0
        r = 0

        while l < n and r < n:
            
            counts[s[r]] += 1

            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1

            cur = r - l + 1
            output = max(cur, output)
            r += 1

        return output