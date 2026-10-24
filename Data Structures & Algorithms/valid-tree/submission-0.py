class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = [] * n
        for i in range(n):
            row = []
            adj.append(row)
         
        visit = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
            
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            
            for j in adj[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
                
            return True


        print(adj[0])

        return (dfs(0, -1) and len(visit) == n)