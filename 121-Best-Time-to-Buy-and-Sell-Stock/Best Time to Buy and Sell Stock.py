class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 忽略[]的情况
        p = 0 
        l = float("inf") 
        
        for each in prices:
            p = max(p, each - l)
            l = min(l, each)
            
        return p