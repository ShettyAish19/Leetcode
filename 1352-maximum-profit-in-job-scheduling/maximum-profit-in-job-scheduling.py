class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        jobs=sorted(zip(startTime,endTime,profit))
        
        dp=[0]*(n+1)

        def bin_search(i,jobs):
            low=i+1
            high=len(jobs)-1
            while low<=high:
                mid=(low+high)//2
                if jobs[mid][0]>=jobs[i][1]:
                    high=mid-1

                else:
                    low=mid+1

            return low

        for i in range(n-1,-1,-1):
            next=bin_search(i,jobs)
            dp[i]=max(dp[i+1],jobs[i][2]+dp[next])

        return dp[0]





        