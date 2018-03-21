class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c2, c1 = cost[-1], cost[-2]
        for i in range(3, len(cost) + 1):
            temp = c1
            c1 = min(c1, c2) + cost[-i]
            c2 = temp
        return min(c1, c2)
        
# Time Limit Exceeded
#         def dp(i):
#             if i >= N:
#                 return 0 if  i > N else cost[i]
#             return min(dp(i + 1), dp(i + 2)) + cost[i]
        
#         N = len(cost) - 1
#         return min(dp(0), dp(1))
    
# 更简洁的
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        mc0 = cost[0]
        mc1 = cost[1]
        for i in range(2, n):
            mc0, mc1 = mc1, min(mc0, mc1) + cost[i]
        return min(mc0, mc1)