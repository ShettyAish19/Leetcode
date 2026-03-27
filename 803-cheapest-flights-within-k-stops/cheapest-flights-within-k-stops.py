import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj={i:[] for i in range(n)}
        for f,t,c in flights:
            adj[f].append((t,c))
        
        edges=k+1

        hp=[(0,src,0)] #cost,src,steps
        d={}

        while hp:
            cost,node,steps=heapq.heappop(hp)
            if node==dst:
                return cost
            if steps>k:
                continue
            for nei,c in adj[node]:
                if (nei,steps) not in d or (cost+c)<d[(nei,steps)]:
                    d[(nei,steps)]=cost+c
                    heapq.heappush(hp,(cost+c,nei,steps+1))

        return -1



        