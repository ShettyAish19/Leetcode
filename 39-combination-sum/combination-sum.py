class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def recur(start,cursum,path):
            if cursum==target:
                ans.append(path[:])
                return

            if cursum>target or start>=len(candidates):
                return

            path.append(candidates[start])
            recur(start,cursum+candidates[start],path)
            path.pop()
            recur(start+1,cursum,path)

        recur(0,0,[])
        return ans
        