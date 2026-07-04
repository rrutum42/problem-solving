class DSU:
    def __init__(self, n: int):
        self.comps = n
        self.parent = [n for n in range(n)]
        self.Size = [1] * n

    def find(self, x):
        # if this is it's own parent
        if self.parent[x] == x:
            return x
        # path compression, get the ultimate parent    
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        # find ultimate parents of u and v 
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        
        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            self.parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        else:
            self.parent[pv] = pu
            self.Size[pu] += self.Size[pu]
        return True

    def components(self):
        return self.comps  

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        no cycles
        fully connected
        '''
        # tree will have n-1 edges for n nodes
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        # all connected to each other
        return dsu.components() == 1

