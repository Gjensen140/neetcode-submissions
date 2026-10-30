from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Idea: Maintain a heap of tuples (count, task, last)

        counts = [0] * 26
        
        for task in tasks:
            counts[ord(task) - ord('A')] -= 1
        

        heap = []
        for i in range(26):
            count = counts[i]
            if count != 0:
                heap.append(count)

        heapify(heap)

        queue = collections.deque()  # stores pairs of (remaining_count, available_time)
        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heappush(heap, count)
            
            
            if heap:
                count = heappop(heap)
                count += 1

                if count != 0:
                    queue.append((count, time + n + 1))
            

        return time