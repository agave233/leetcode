class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return range(1,n + 1)
        
        res, t = [], 1
        for i in range(k):
            if i % 2 == 0:
                res.append(t)
                t += 1
            else:
                res.append(n - res[-1] + 1)
                
        if k % 2 == 0:
            return res + range(res[-1] - 1, res[-2], -1)
        return res + range(res[-1] + 1, res[-2])