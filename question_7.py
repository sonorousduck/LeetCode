class Solution:
    # For some reason, checking the length of the array and stopping if you hit that point
    # actually made it slower. Probably depends on the lists you are using.
    def maxProfit(self, prices: list[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        purchase_price = prices[0]
        best_profit = 0
        
        
        
        for i in range(1, len(prices)):
            profit = prices[i] - purchase_price
            if profit > best_profit:
                best_profit = profit
            
            if prices[i] < purchase_price:
                purchase_price = prices[i] 
        
        return best_profit
        
        
        
        
    
    
           
        

                
            
        

if __name__ == "__main__":
    test = Solution()
    nums = [7,1,5,3,6,4]
    print(test.maxProfit(nums))
    
    nums = [7,6,4,3,1]
    print(test.maxProfit(nums))

