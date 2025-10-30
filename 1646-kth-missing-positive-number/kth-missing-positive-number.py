class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j=1
        i=0
        count=0
        n=len(arr)
        while i<n:
            if arr[i]==j:
                j+=1
                i+=1

            else:
                count+=1
                if count==k:
                    return j
                j+=1

        if count==0:
            return arr[n-1]+k

        elif count<k:
            return arr[n-1]+(k-count)

            
            

        
                
