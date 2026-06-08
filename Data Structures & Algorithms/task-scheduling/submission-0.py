from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(m) <- m is num of tasks, O(26) = O(1)
        counts = Counter(tasks)
        maxHeap = [-val for val in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        #cooldwon q [[remaining_count, time + n]]
        q = deque()
        while maxHeap or q:
            '''
            1. time ++ 
            2. pop highest freq elem from heap
            3. reduce the val - 1 
            4. put in cooldown q if val > 0
            5. if any elem in cooldown q is ready then push it on heap
            6. if maxHeap is empty then forward time to time of first elem in q
            '''
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                # -3 + 1 = -2
                task_remaining_count = 1 + heapq.heappop(maxHeap)
                if task_remaining_count:
                    q.append([task_remaining_count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time        
         

            
        