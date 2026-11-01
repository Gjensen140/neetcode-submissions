class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s_p = 0
        t_p = 0

        while t_p < len(t):
            
            if s[s_p] == t[t_p]:
                s_p += 1


            if s_p == len(s):
                return True
            
            t_p += 1

        return False
