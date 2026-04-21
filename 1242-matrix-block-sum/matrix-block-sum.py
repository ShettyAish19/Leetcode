class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        ans=[[0]*n for i in range(m)]
        for i in range(m):
          for j in range(n):
            startr,endr=max(0,i-k),min(m-1,i+k)
            startc,endc=max(0,j-k),min(n-1,j+k)

            total=0
            for r in range(startr,endr+1):
                for c in range(startc,endc+1):
                    total+=mat[r][c]
            ans[i][j]=total

        return ans

            

     
    
    

    

    

                
                
            
        
        