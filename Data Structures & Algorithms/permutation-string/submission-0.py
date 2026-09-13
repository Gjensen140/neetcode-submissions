from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Initialize variables to count permutations
        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)

        # Setting up our first counter
        for c in s1:
            s1_counter[c] += 1
        
        # Initializing variables to iterate through s2
        n1 = len(s1)
        n2 = len(s2)
        start = 0
        cur = 0

        while cur < n2:
            # Incrementing the count for the character
            s2_counter[s2[cur]] += 1

            # Adjusting window if longer than the first string
            if (cur - start + 1) > n1:
                s2_counter[s2[start]] -= 1
                if s2_counter[s2[start]] == 0:
                    del s2_counter[s2[start]]

                start += 1

            if s2_counter == s1_counter:
                return True

            cur += 1
        
        return False