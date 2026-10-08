class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #for each int calculate the profit by using a pointer
        #if number to the right is less then adjust the pointer, if number is greater then begin couting profit until the number isnt greater then the one to the right
        l = 0 
        r = 1
        maxProfit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                potentialProfit = prices[r] - prices[l]
                maxProfit = max(potentialProfit, maxProfit)
            if prices[l] >= prices[r]:
                l=r
            r+=1
       
        return maxProfit