class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for R in range(len(prices)):
            L  = 0
            while L < R:
                profit = max(profit, prices[R] - prices[L])  
                L += 1

                

                
        return profit
