class Solution:
    def checkValidString(self, s: str) -> bool:
        '''def backtrack(index,balanced):
            if balanced<0:
                return False

            if index==len(s) :
                return balanced==0

            char=s[index]
            if char=='(':
                return backtrack(index+1,balanced+1)

            elif char==')':
                return backtrack(index+1,balanced-1)

            else:
                return backtrack(index+1,balanced+1) or backtrack(index+1,balanced-1) or backtrack(index+1,balanced)

        return backtrack(0,0)'''

        low=0
        high=0
        for char in s:
            if char=='(':
                low+=1
                high+=1

            elif char==')':
                low-=1
                high-=1

            else:
                low-=1
                high+=1

            if high<0:
                return False

            if low<0:
                low=0

        return low==0

            
        

        