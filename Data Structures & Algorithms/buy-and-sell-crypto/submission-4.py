class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0

        for r in range(1, len(prices)):
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r

            max_profit = max(max_profit, curr_profit)

        return max_profit

