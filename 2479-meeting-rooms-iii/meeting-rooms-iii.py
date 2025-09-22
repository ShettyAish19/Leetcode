class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        empty=[]
        full=[]
        for i in range(n):
            heapq.heappush(empty,i)

        count=[0]*n

        for start,end in meetings:
            duration=end-start
            while full and full[0][0]<=start:
                end_time,room=heapq.heappop(full)
                heapq.heappush(empty,room)

            if empty:
                room=heapq.heappop(empty)
                heapq.heappush(full,(end,room))

            else:
                end_time,room=heapq.heappop(full)
                new_end=end_time+duration
                heapq.heappush(full,(new_end,room))

            count[room]+=1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i

            
        