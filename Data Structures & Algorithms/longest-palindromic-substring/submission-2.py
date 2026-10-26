class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        output = s[0]

        for i in range(n-1):

            # Even Palindromes
            if s[i] == s[i+1]:
                l = i - 1
                r = i + 2
                cur = s[i:i+2]
                while l >= 0 and r < n and s[l] == s[r]:
                    cur = s[l:r + 1]
                    l -= 1
                    r += 1

                if len(output) < len(cur):
                    output = cur
            
            # Odd palindromes
            if i > 0 and s[i-1] == s[i+1]:
                l = i - 2
                r = i + 2
                cur = s[i-1:i+2]
                while l >= 0 and r < n and s[l] == s[r]:
                    cur = s[l:r+1]
                    l -= 1
                    r += 1

                if len(output) < len(cur):
                    output = cur
        
        return output
