class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i:[] for i in range(n)}
        for n1,n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)
        
        print(nodes)
        visit = set()
        def dfs(node):
            for n in nodes[node]:
                if n not in visit:
                    visit.add(n)
                    dfs(n)

        res = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res +=1
        
        return res
'''

'''                