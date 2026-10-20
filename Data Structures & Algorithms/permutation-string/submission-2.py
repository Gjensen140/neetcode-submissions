class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        n = len(s2)

        chrs_s1 = [0] * 26

        for c in s1:
            chrs_s1[ord(c) - ord('a')] += 1

        l = 0
        chrs_s2 = [0] * 26

        for r in range(n):
            
            if r - l + 1 > m:
                chrs_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            chrs_s2[ord(s2[r]) - ord('a')] += 1

            if chrs_s2 == chrs_s1:
                return True

        return False