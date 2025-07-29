class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        if numRows==1:
            return [[1]]

        
        for i in range(numRows):
            res=[]
            for j in range(i+1):
                if j==0 or j==i:
                    res.append(1)

                else:
                    res.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(res)

        return ans


        