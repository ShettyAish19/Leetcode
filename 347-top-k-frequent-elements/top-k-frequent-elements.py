from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucketsort
        count=Counter(nums)
        bucket_list=[[] for i in range(len(nums)+1)]

        for num,freq in count.items():
            bucket_list[freq].append(num)

        res=[]
        for freq in range(len(bucket_list)-1,0,-1):
            for num in bucket_list[freq]:
                res.append(num)

                if len(res)==k:
                    return res


        



        