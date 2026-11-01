class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = [0] * 26
        max_ind = -1

        for c in s:
            counts[ord(c) - ord('a')] += 1

        largest = max(counts)
        
        # Impossible case
        if largest > (n+1)//2:
            return ""

        max_ind = counts.index(largest)
        output = [""] * n
        cur = 0

        while counts[max_ind] > 0:
            output[cur] = chr(ord('a') + max_ind)
            cur += 2
            counts[max_ind] -= 1

            if cur >= n:
                cur = 1
        
        for i in range(26):
            
            while counts[i] > 0:
                output[cur] = chr(ord('a') + i)
                counts[i] -= 1
                cur += 2
                if cur >= n:
                    cur = 1

        return "".join(output)