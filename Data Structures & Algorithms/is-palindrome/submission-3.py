class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                print(s[l])
                print(s[r])
                return False

            l += 1
            r -= 1

        return True