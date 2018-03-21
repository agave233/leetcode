class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 0 else int(n == 0)
        
        path = [1, 2]
        for i in range(2, n):
            path.append(path[i - 1] + path[i - 2])
        return path[n - 1] if n else 0 