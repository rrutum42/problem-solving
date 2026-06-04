class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        d = {i:[] for i in range(n)}
        for n1,n2 in edges:
            d[n1].append(n2)
            d[n2].append(n1)
        # print(d)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for neigh in d[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh,node): 
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)
        

'''
connected acyclic graph
1. check if we can reach each node from each node 
2. no cycles
3. nodes = edges + 1

create an adjacency list
visited set 
dfs 
if node already in visited return false
if node[]
'''        