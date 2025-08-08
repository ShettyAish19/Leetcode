class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        top,bottom=0,r-1
        while top<=bottom:
            mid=(top+bottom)//2
            if matrix[mid][0]<=target<=matrix[mid][c-1]:
                break

            if matrix[mid][0]>target:
                bottom=mid-1

            else:
                top=mid+1

        if top>bottom:
            return False

        row=(top+bottom)//2

        l, h = 0, c-1
        
        while l <= h:
            mid = (l + h) // 2
            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid]<target:
                l=mid+1
            else:
                h=mid-1
                    
        return False
        