class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        ans=[[0]*n for i in range(m)]
        '''for i in range(m):
          for j in range(n):
            startr,endr=max(0,i-k),min(m-1,i+k)
            startc,endc=max(0,j-k),min(n-1,j+k)

            total=0
            for r in range(startr,endr+1):
                for c in range(startc,endc+1):
                    total+=mat[r][c]
            ans[i][j]=total

        return ans'''


        prefix=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j]=mat[i][j]
                if i>0:
                    prefix[i][j]+=prefix[i-1][j]

                if j>0:
                    prefix[i][j]+=prefix[i][j-1]

                if i>0 and j>0:
                    prefix[i][j]-=prefix[i-1][j-1]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(m-1, i+k)
                c2 = min(n-1, j+k)
                
                total = prefix[r2][c2]
                
                if r1 > 0:
                    total -= prefix[r1-1][c2]
                if c1 > 0:
                    total -= prefix[r2][c1-1]
                if r1 > 0 and c1 > 0:
                    total += prefix[r1-1][c1-1]
                
                ans[i][j] = total
        
        return ans


            

     
    
    

    

    

                
                
            
        
        