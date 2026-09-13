from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        l = 1001
        r = -1001

        for num in nums:
            count[num] += 1
            l = min(num, l)
            r = max(num, r)
        
        print(l)
        print(r)

        output = []
        for i in range(k):
            highest = [-1 ,0]
            for j in range(l, r + 1):
                if count[j] > highest[1]:
                    highest[0] = j
                    highest[1] = count[j]
            
            output.append(highest[0])
            count[highest[0]] = 0

        return output