# Topological sort
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = []
        for i in range(numCourses):
            l = []
            adj.append(l)

        seen = set()
        first = -1

        for c1, c2 in prerequisites:
            
            if first == -1:
                first = c2
            
            adj[c2].append(c1)

        def dfs(c):
            if c in seen:
                return False
            if adj[c] == []:
                return True

            seen.add(c)
            for course in adj[c]:

                if not dfs(course):
                    return False

            seen.remove(c)
            adj[c] = []
            
            return True

        for i in range(numCourses):
            if not adj[i]:
                continue
            
            if not dfs(i):
                return False

        return True