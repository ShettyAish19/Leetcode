class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        n=len(prices)
        m=len(discounts)
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        p=0
        i=0
        j=0
        while i<n and j<m:
            p+=(prices[i]*(100-discounts[j]))/100
            i+=1
            j+=1


        while i<n:
            p+=prices[i]
            i+=1

        return p
            

        