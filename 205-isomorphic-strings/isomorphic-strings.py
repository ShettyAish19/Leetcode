class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        d={}
        st=set()
        i=0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
                if t[i] not in st:
                    st.add(t[i])
                else:
                    return False
            elif d[s[i]] !=t[i]:
                return False

        return True

        
        