class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.Size = [1] * (n+1)
    
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if self.parent[pu] == self.parent[pv]:
            return False # cycle detected
        
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return True 


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]

        