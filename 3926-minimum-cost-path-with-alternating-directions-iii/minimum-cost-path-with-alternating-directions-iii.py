import heapq
class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        hp=[]
        hp.append((1,0,0,1)) #next_parity ->0-even and 1- odd parity

        dist=[[[float('inf')]*2 for _ in range(n)] for _ in range(m)]
        dist[0][0][1]=1  #cost 

        d=[(-1,0),(0,-1),(1,0),(0,1)]
    
        while hp:
            cost,r,c,par=heapq.heappop(hp)

            if cost >dist[r][c][par]:
                continue

            if r==m-1 and c==n-1:
                return cost

            for dr,dc in d:
                violates=False
                nr,nc=r+dr,c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                if par==1 and (dr==-1 or dc==-1):
                    violates=True

                elif par==0 and (dr==1 or dc==1):
                    violates=True

                next_cost=cost+(nr+1)*(nc+1)
                if violates:
                    next_cost+=penalty[r][c]

                new_par=1-par

                if next_cost<dist[nr][nc][new_par]:
                    dist[nr][nc][new_par]=next_cost

                    heapq.heappush(hp,(next_cost,nr,nc,new_par))

            wait_cost = cost + penalty[r][c]
            new_par = 1 - par

            if wait_cost < dist[r][c][new_par]:
                dist[r][c][new_par] = wait_cost
                heapq.heappush(
                    hp,
                    (wait_cost, r, c, new_par)
                )




            






        
        