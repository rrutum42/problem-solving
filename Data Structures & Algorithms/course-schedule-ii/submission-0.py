class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(V+E),O(V+E) 
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src,dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        finished = 0
        while q:
            node = q.popleft()
            res.append(node)
            finished += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        res.reverse()
        return res if (finished==numCourses) else []

        