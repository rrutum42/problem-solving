class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # BFS
        adj = {c: [] for w in words for c in w}
        n = len(words)
        indegree = {c: 0 for c in adj}


        for i in range(n-1):
            w1,w2=(words[i]), (words[i+1])
            smaller = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:smaller] == w2[:smaller]:
                return ""
            for j in range(smaller):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w2[j]] +=1
                    break

        print(adj)
        print(indegree)

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for neigh in adj[node]:
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    q.append(neigh)
        print(res)
        # cycle detected
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)

        # DFS
        # adj = {c: [] for w in words for c in w}
        # n = len(words)

        # for i in range(n-1):
        #     w1,w2=(words[i]), (words[i+1])
        #     smaller = min(len(w1),len(w2))
        #     if len(w1) > len(w2) and w1[:smaller] == w2[:smaller]:
        #         return ""
        #     for j in range(smaller):
        #         if w1[j] != w2[j]:
        #             adj[w1[j]].append(w2[j])
        #             break
        # visited = {}
        # # visited
        # # 0 -> not visited
        # # 1 -> visiting
        # # 2 -> visited
        # stk = []
        # def dfs(c):
        #     if visited.get(c, 0) == 1:
        #         return False  # cycle detected
        #     if visited.get(c, 0) == 2:
        #         return True   # already processed

        #     visited[c] = 1  # mark as visiting
        #     for nei in adj[c]:
        #         if not dfs(nei):
        #             return False
        #     visited[c] = 2  # mark as visited
        #     stk.append(c)   # postorder append
        #     return True

        # # topological sort
        # for a in adj:
        #     if visited.get(a, 0) == 0:
        #         if not dfs(a):
        #             return ""  # cycle found
        # stk.reverse()
        # return "".join(stk)   



        