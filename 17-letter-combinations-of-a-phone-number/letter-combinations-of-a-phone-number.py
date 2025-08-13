class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return res
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def backtrack(start,path):
            if len(path)==len(digits):
                res.append(path[:])
                return

            for char in d[digits[start]]:
    
                backtrack(start+1,path+char)
                

        backtrack(0,"")
        return res