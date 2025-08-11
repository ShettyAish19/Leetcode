class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        '''def backtrack(start,cursum,path):
            if cursum==target:
                ans.append(path[:])
                return

            if start>=len(candidates) or cursum>target:
                return
            path.append(candidates[start])
            backtrack(start+1,cursum+candidates[start],path)

            path.pop()

            while start+1<len(candidates) and candidates[start]==candidates[start+1]:
                start+=1
            backtrack(start+1,cursum,path)'''

        def backtrack(start,cursum,path):
            if cursum==target:
                ans.append(path[:])
                return

            if cursum>target:
                return

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,cursum+candidates[i],path)
                path.pop()



        
        backtrack(0,0,[])
        return ans
        