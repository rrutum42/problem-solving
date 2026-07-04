class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(V+E), O(V+E)
        # kahn's algo
        ans = []

        # num of prerequisites for each course
        indegree = [0]*numCourses
        # src -> [dests]
        adj = [[] for i in range(numCourses)]

        for src,dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        '''
        numCourses=3
        prerequisites=[[1,0]]
        '''
        # print(indegree)
        # print(adj)
        '''
        [1, 0, 0]
        [[], [0], []]
        '''
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            ans.append(course)

            for neigh in adj[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        ans.reverse()
        if len(ans) == numCourses:
            return ans
        return []
