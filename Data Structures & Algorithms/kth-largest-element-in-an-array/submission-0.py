
from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]

        heapify(heap)

        for i in range(k - 1):
            heappop(heap)

        return -heappop(heap)