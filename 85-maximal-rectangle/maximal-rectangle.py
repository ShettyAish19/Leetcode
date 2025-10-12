class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m=len(matrix),len(matrix[0])
        maxi=0
        heights=[0]*m
        def max_area(heights,m):
            maxi=0
            st=[]
            temp=heights+[0]
            for i in range(m+1):
                while st and temp[st[-1]]>temp[i]:
                    h=temp[st.pop()]

                    if st:
                        width=i-st[-1]-1

                    else:
                        width=i

                    maxi=max(maxi,h*width)
                st.append(i)

            return maxi

        for r in range(n):
            for c in range(m):
                if matrix[r][c]=='1':
                    heights[c]+=1

                else:
                    heights[c]=0

            maxi=max(maxi,max_area(heights,m))
        return maxi


       

        