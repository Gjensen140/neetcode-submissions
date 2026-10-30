class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for i in range(k + 1):
            temp = costs.copy()

            for s, d, c in flights:
                # s = source, d = dest, c = cost
                if costs[s] == float('inf'):
                    continue
                elif costs[s] + c < temp[d]:
                    temp[d] = costs[s] + c
                
            costs = temp
        
        if costs[dst] == float('inf'):
            return -1
        
        return costs[dst]
