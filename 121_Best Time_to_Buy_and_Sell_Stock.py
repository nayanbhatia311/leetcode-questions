class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_number=float('inf')

        for index in range(len(prices)):
            if min_number>prices[index]:
                min_number=prices[index]

            elif prices[index]-min_number>max_profit:
                max_profit=prices[index]-min_number
