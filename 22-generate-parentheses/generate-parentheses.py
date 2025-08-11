class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def recur(ans,op,cl):
            if len(ans)==2*n:
                res.append(ans)
                return
            
            if op<n:
                recur(ans+'(',op+1,cl)
            

            if cl<op:
                
                recur(ans+')',op,cl+1)
                
        recur("",0,0)
        return res
        