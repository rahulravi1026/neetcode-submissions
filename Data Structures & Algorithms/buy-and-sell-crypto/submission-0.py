class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = prices[0]
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            result = max(result, price - minPrice)
        return result