from typing import List

class DSU:
    def __init__(self, n: int):
        # Time Complexity: O(N) - Initializes loops of size N to set up arrays
        # Space Complexity: O(N) - Allocates memory for parent and Size arrays
        self.comps = n
        self.parent = [n for n in range(n)]
        self.Size = [1] * n

    def find(self, x):
        # Time Complexity: O(α(N)) amortized - Due to path compression, trees are flattened, 
        # making subsequent lookups nearly constant O(1).
        # Space Complexity: O(log N) - Maximum recursion stack frame size bounded by Union by Size.
        
        # if this is it's own parent
        if self.parent[x] == x:
            return x
        # path compression, get the ultimate parent    
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        # Time Complexity: O(α(N)) amortized - Relies on two find() operations and constant time pointer updates.
        # Space Complexity: O(log N) - Max stack space inherited from the find() recursion calls.
        
        # find ultimate parents of u and v 
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False # Cycle detected
        
        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            self.parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        else:
            self.parent[pv] = pu
            self.Size[pu] += self.Size[pv] # FIXED: Changed from self.Size[pu] to self.Size[pv]
        return True

    def components(self):
        # Time Complexity: O(1) - Simply returns a pre-computed variable.
        # Space Complexity: O(1) - No extra space utilized.
        return self.comps  

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        ======================================================================
        MAIN COMPLEXITY ANALYSIS:
        Let N be the number of nodes (n) and E be the number of edges (len(edges)).
        
        TOTAL TIME COMPLEXITY: O(N + E * α(N))
        - O(N) to initialize the DSU structures.
        - O(E * α(N)) to iterate through the edges and perform union-find.
        - Because the condition 'len(edges) > n - 1' filters out any input where 
          E >= N, E is strictly less than N when the loop runs. Thus, this 
          effectively runs in near-linear time: O(N).
        
        TOTAL SPACE COMPLEXITY: O(N)
        - The DSU tracking arrays ('parent' and 'Size') require O(N) space.
        - The recursion stack for 'find' requires O(log N) space.
        - O(N) dominates the space complexity.
        ======================================================================
        '''
        # tree will have n-1 edges for n nodes
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            # If union returns False, a cycle is found
            if not dsu.union(u, v):
                return False
        
        # All nodes must be fully connected into exactly 1 component
        return dsu.components() == 1