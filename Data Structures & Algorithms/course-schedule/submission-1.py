class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for crs,p in prerequisites:
            preq[crs].append(p)
        # print(preq)
        visit = set()

        def dfs(crs):
            # cycle detected
            if crs in visit:
                return False
            # base conditn
            if preq[crs] == []:
                return True
            
            visit.add(crs)
            # visit all preq of crs
            for p in preq[crs]:
                if not dfs(p): return False
            visit.remove(crs)
            preq[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


'''
identify if graph has cycle

for each [a,b] create a graph. 
increment doable += 1
modify the same graph for each [a,b]
if a cycle is detected, break the search
return doable >= numCourses

create a hashmap of course to [pre]

iterate over each course 0 to numCourses -1
for each course if it is already in visit then return false
if no prereq exist for it then return true

add the node to visitset
for each of the nodes preqs, run dfs
backtrack, remove the node from visit set 
make the preq of node empty
return True

run dfs for every course 0 to numCourses - 1
'''        