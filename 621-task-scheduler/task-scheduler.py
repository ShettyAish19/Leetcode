from collections import Counter,deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f=Counter(tasks)
        q=deque()
        max_heap=[-cnt for cnt in f.values()]
        heapq.heapify(max_heap)
        time=0

        while max_heap or q:
            time+=1
            if max_heap:
                cnt=1+heapq.heappop(max_heap)
                if cnt:
                    q.append((time+n,cnt))

            if q and q[0][0]==time:
                ready_time,rem_cnt=q.popleft()
                heapq.heappush(max_heap,rem_cnt)

        return time 



        