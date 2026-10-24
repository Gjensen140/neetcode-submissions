# Idea: Levels order traversal
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        
        degrees = [0] * n

        # Making Adjacency list
        adj = []
        for i in range(n):
            t = []
            adj.append(t)


        for c1, c2 in prerequisites:
            adj[c2].append(c1)
            degrees[c1] += 1

                        
        queue = collections.deque()
        output = []

        for i in range(n):
            if degrees[i] == 0:
                queue.append(i)

        if not queue and prerequisites:
            return []
        
        while queue:
            course = queue.popleft()

            output.append(course)

            for c in adj[course]:
                degrees[c] -= 1

                if degrees[c] == 0:
                    queue.append(c)

        for d in degrees:
            if d != 0:
                return []

        return output