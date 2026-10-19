class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l = 0
        cur_large = 0
        maxf = 0 
        chrs = [0] * 26

        for r in range(n):
            
            chrs[ord(s[r]) - ord('A')] += 1
            cur_large = max(cur_large, chrs[ord(s[r]) - ord('A')])
            maxf = max(maxf, cur_large)
            

            diff = r - l + 1 
            while diff - cur_large > k: 
                chrs[ord(s[l]) - ord('A')] -= 1
                cur_large = max(chrs)
                l += 1
                diff = r - l + 1
                
        
        return min(n, (maxf + k))
            
            