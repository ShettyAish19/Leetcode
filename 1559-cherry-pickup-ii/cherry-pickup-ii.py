class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def f(i,j1,j2):
            if j1<0 or j1>=n or j2<0 or j2>=n:
                return float('-inf')
            if (i,j1,j2) in memo:
                return memo[(i,j1,j2)]

            if i==m-1:
                if j1!=j2:
                    return grid[i][j1]+grid[i][j2]

                else:
                    return grid[i][j1]

            maxi=float('-inf')
        

            for k1 in (j1-1,j1,j1+1):
                for k2 in (j2-1,j2,j2+1):
                    
                    maxi=max(maxi,f(i+1,k1,k2))

                  

            if j1!=j2:
                maxi+=grid[i][j1]+grid[i][j2]

            else:
                maxi+=grid[i][j1]
            memo[(i,j1,j2)]=maxi
            return maxi

        memo={}
        return f(0,0,n-1)


            
        