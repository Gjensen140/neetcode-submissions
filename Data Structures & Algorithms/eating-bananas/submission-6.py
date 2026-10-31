class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l = 1
        r = max(piles)
        output = r

        while l <= r:
            m = (r + l) // 2


            time = 0
            for p in piles:
                time += math.ceil(float(p) / m)

            if time <= h:
                output = min(output, m)
                r = m - 1
            else:
                l = m + 1

        return output 
