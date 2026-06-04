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
for each node check if it is already in visited set
if it is then cycle
if it is not then add to the visited set 
check for dfs of each of it's neighbors.
because its an undirected graph, we need to maintain a prev value as well.
when we dfs the neighbor j after we have processed the node i, 
even node i will be a part of the neighbors of j. so ignore i and check for all other sneighbors
pt 2 is ensured by dfs
for pt 1, after dfs check is visited length == n
'''        