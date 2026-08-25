class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        def f(mask,last):
            if dp[mask][last]!=-1:
                return dp[mask][last]
            if mask==(1<<last):
                arrival,floor=requests[last][0],requests[last][1]
                dp[mask][last]=max(arrival,abs(start-floor))
                return dp[mask][last]

            ans=float('inf')
            prev_mask=mask^(1<<last)

            for prev in range(k):
                if prev_mask & (1<<prev):
                    prev_time= f(prev_mask,prev)

                    travel_time=prev_time+abs(requests[prev][1]-requests[last][1])
                    current_time=max(requests[last][0],travel_time)
                    ans=min(ans,current_time)
            dp[mask][last]=ans
            return ans

        
        k=len(requests)
        full_mask=(1<<k)-1

        ans=float('inf')

        dp=[[-1]*k for _ in range(1<<k)]
        
        for last in range(k):
            ans=min(ans,f(full_mask,last))

        return ans
                

        