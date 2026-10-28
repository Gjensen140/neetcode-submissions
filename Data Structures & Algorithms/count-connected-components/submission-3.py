class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while uf[res] != res:
                uf[res] = uf[uf[res]]
                res = uf[res]
            
            return res

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            elif rank[p2] > rank[p1]:
                uf[p1] = p2
                rank[p2] += rank[p1]
            else:
                uf[p2] = p1
                rank[p1] += rank[p2]
            
            return 1

            
        output = n

        for n1, n2 in edges:
            output -= union(n1,n2)

        return output

