class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=len(nums)
        def recur(start,path):
            l.append(path[:])
            for i in range(start,n):
                path.append(nums[i])
                recur(i+1,path)
                path.pop()

        recur(0,[])
        return l
        

            





        