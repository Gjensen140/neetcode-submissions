from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)

        heap = []
        for i in range(n):
            x,y = points[i]
            dist = math.sqrt((x**2) + (y**2))

            heap.append((dist, x, y))

        heapify(heap)

        output = []
        for i in range(k):
            d, x, y = heappop(heap)

            output.append([x,y])

        return output