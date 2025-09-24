class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        i=0
        l=[]
        while i<n and intervals[i][1]<newInterval[0]:
            l.append(intervals[i])
            i+=1

        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            
            i+=1
        l.append(newInterval)

        while i<n :
            l.append(intervals[i])
            i+=1

        return l

        