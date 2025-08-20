class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        pref_count=defaultdict(int)
        pref_count[0]=1
        cursum=0
        count=0
        for num in   nums:
            cursum+=num
            count+=pref_count[cursum-goal]
            pref_count[cursum]+=1
        return count

                


                    

                
                    





        