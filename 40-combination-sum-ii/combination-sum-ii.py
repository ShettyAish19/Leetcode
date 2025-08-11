class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def backtrack(start,cursum,path):
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
            backtrack(start+1,cursum,path)

        
        backtrack(0,0,[])
        return ans
        