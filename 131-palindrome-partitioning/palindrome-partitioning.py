class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def is_pal(s):
            return s==s[::-1]
        
        def backtrack(start,path):
            if start==len(s):
                ans.append(path[:])
                return 

            for i in range(start,len(s)):
                substring=s[start:i+1]
                if is_pal(substring):
                    path.append(substring)
                    backtrack(i+1,path)
                    path.pop()

        backtrack(0,[])
        return ans 