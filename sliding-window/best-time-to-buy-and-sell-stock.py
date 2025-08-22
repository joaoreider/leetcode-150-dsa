from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell

        maxProfit = 0

        while r < len(prices):

            # check if is it a profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: 
                l = r 
            r += 1

        return maxProfit

