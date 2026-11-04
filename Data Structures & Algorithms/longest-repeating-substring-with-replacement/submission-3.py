class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        chrs = [0] * 26
        
        l = 0
        output = 0
        highest = 0


        for r in range(n):

            chrs[ord(s[r]) - ord('A')] += 1
            highest = max(chrs[ord(s[r]) - ord('A')], highest)

            # Slide
            while (r - l + 1) - highest > k:

                chrs[ord(s[l]) - ord('A')] -= 1
                highest = max(chrs[ord(s[l]) - ord('A')], highest)
                l += 1
                print(highest)

                

            size = r - l + 1
            output = max(size, output)

        return min(output, n)