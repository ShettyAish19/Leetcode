class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxi=0
        heights.append(0)
        for i,num in enumerate(heights):
            #find smallest number to the right of a number
            while st and heights[st[-1]]>num:
                h=heights[st.pop()]
                if st:
                    width=i-st[-1]-1

                else:
                    width=i

                maxi=max(maxi,h*width)

            st.append(i)

        return maxi



                


        