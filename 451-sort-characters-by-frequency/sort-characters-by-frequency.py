class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for j in s:
            if j in d:
                d[j]+=1
            else:
                d[j]=1

        s_d=sorted(d.items(),key=lambda x:-x[1])

        st=""
        for j,k in s_d:
            st+=(j*k)

        return st


        