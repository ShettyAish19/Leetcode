class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

     

        def dfs(index,path,cur_sum,last):
            if index==n:
                if cur_sum==target:
                    res.append(path)
                    return 

            for j in range(index,n):
                if j>index and num[index]=='0':
                    break

                subs=num[index:j+1]
                cur=int(subs)

                if index==0:
                    dfs(j+1,subs,cur,cur)

                else:
                    dfs(j+1,path+'+'+subs,cur_sum+cur,cur)

                    dfs(j+1,path+'-'+subs,cur_sum-cur,-cur)

                    dfs(j+1,path+'*'+subs,cur_sum-last+last*cur,last*cur)

        res=[]
        n=len(num)
        dfs(0," ",0,0)
        return res

        


        