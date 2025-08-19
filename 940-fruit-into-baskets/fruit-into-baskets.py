from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d=defaultdict(int)
        start=0
        maxi=0
        k=2
        for end in range(len(fruits)):
          if   fruits[end] not in d :
            d[fruits[end]]=1
            k-=1
          
          elif fruits[end] in d:
            d[fruits[end]]+=1

          while k<0:
            d[fruits[start]]-=1
            
            if d[fruits[start]]==0:
              del d[fruits[start]]
              k+=1
            start+=1

          maxi=max(maxi,sum(d.values()))

        return maxi
        