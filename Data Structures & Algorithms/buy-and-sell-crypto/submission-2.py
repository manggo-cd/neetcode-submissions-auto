class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Profit is just the max number when you subtract greatest number
        # in sequence from a previous lower number in sequence

        rsf = 0

        if not prices:
            return 0
        
        left = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[left]
            if profit < 0:
                left = i
            elif profit > rsf:
                rsf = profit
        return rsf



        