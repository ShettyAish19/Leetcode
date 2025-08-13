class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,path,cursum):
            if len(path)==k and cursum==n:
                ans.append(path[:])
                return 

            if start>9 or len(path)>k or cursum>n:
                return
            
            path.append(start)
            backtrack(start+1,path,cursum+start)
            path.pop()
            backtrack(start+1,path,cursum)
        
        backtrack(1,[],0)
        return ans

        
        