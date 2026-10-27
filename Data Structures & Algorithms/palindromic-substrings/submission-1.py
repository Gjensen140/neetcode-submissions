class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        output = n
        #seen = set()

        def expand(l, r):
            nonlocal output
            while l >= 0 and r < n and s[l] == s[r]:# and (l,r) not in seen:
                #seen.add((l,r))
                output += 1
                l -= 1
                r += 1

            
        for i in range(0, n - 1):
            if s[i] == s[i + 1]:
                expand(i, i + 1)
            if i > 0 and s[i - 1] == s[i + 1]:
                expand(i - 1, i + 1)
            
        return output

                