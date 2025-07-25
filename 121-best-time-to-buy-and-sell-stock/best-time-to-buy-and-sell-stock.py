class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        n=len(prices)
        min_price=prices[0]
        for i in range(1,n):
            if prices[i]-min_price>max_p:
                max_p=prices[i]-min_price
            if prices[i]<min_price:
                min_price=prices[i]

        return max_p
        