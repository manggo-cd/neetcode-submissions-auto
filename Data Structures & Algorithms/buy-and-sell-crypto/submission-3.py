class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Profit is just the max number when you subtract greatest number
        # in sequence from a previous lower number in sequence

        rsf = 0
        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                rsf = max(rsf, profit)

        return rsf



        