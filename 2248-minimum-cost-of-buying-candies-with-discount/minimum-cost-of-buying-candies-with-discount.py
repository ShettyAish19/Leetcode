class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n=len(cost)
        if n==1:
            return cost[0]
        
        cost.sort(reverse=True)
        
        ans=0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                ans += cost[i]
                
        return ans

        