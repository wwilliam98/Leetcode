class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        #just keep finding the valley and peak for each part
        while i < len(prices)-1:
            #when the slopes is going down
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            
            #when the slopes is going up
            while i < len(prices) -1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            
            max_profit += peak - valley
        return max_profit