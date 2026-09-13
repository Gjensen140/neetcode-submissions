from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # Only one character
        if n < k or n <= 1:
            return n

        # Initializing character counter
        counts = defaultdict(int)
        counts[s[0]] += 1

        # Initializing variables to track position
        start = 0
        end = 1

        # Initializing variables to track frequency and highest width
        output = 1
        max_freq = 0

        # Iterating through the string
        while end < n:
            # Incrementing the counter for the current string
            counts[s[end]] += 1
            max_freq = max(max_freq, counts[s[end]])

            # Current Width
            w = end - start + 1

            # We violate the k replacements
            while w - max_freq > k:
                counts[s[start]] -= 1
                start += 1
                w -= 1

            output = max(w, output)
            end = end + 1
        
        return output