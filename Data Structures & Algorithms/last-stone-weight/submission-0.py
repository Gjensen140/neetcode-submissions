from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)

        while len(heap) > 1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            
            if s1 == s2:
                continue
            
            heappush(heap, (s1 - s2))

        if len(heap) == 1:
            return (-1 * heap[0])
        else:
            return 0