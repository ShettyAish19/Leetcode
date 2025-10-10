class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while st and st[-1]>i and k>0:
                st.pop()
                k-=1

            if i=='0' and not st:
                continue

            st.append(i)

        while k>0 and st:
            st.pop()
            k-=1


        return "".join(st) if st else "0"
            

            