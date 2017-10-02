class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        top,bot = [],[]
        i=0
        while(i<len(prices)-1):
            if prices[i+1] == prices[i]:
                prices.pop(i)
            else:
                i += 1
        if len(prices)<2:
            return 0   
        if prices[0]<prices[1]:
            bot.append(0)
        for i in range(1,len(prices)-1):
            if prices[i-1]<prices[i] and prices[i+1] < prices[i]:
                top.append(i)
            elif prices[i-1]>prices[i] and prices[i+1]>prices[i]:
                bot.append(i)
        if prices[-1]>prices[-2]:
            top.append(len(prices)-1)
        
        if not (top and bot):
            return 0
        
        profit = 0
        sell = 0
        for idx,buy in enumerate(bot):
            if (idx==0 or prices[bot[idx]]<prices[bot[idx-1]]):
                profit = max([profit,max([prices[i] for i in top[sell:]])-prices[buy]])
            sell += 1
                
        return profit

ins = Solution()
print(ins.maxProfit([7, 1, 5, 3, 6, 4]))
