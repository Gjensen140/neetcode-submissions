class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if not s:
            return True
        
        s_p = 0
        t_p = 0

        while t_p < n:
            
            if s[s_p] == t[t_p]:
                s_p += 1


            if s_p == m:
                return True
            
            t_p += 1

        return False
