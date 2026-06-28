class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = -float("inf")
        lowest = float('inf')

        for price in prices:
            lowest = min(lowest,price)
            mp = max(mp,price-lowest)
        return mp


        