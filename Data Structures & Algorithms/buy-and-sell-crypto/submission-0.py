class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxdiff = 0
        for n in prices:
            if n < min:
                min = n
            maxdiff = max(maxdiff, n-min)
        return maxdiff