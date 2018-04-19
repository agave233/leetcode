# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 问总共有多少条不同的路径？

# 例如，上图是一个7 x 3 的网格。有多少可能的路径？

# 说明：m 和 n 的值均不超过 100。

# 示例 1:

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0 if i < n - 1 else 1 for i in range(n)] if j < m - 1 else [1] * n for j in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                res[i][j] += res[i + 1][j] + res[i][j + 1]
        return res[0][0]


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        j=min(m-1,n-1)
        if j==0:
            return 1
        k=m+n-2
        res1=1
        res2=1
        for i in range(j):
            res1*=k-i
            res2*=j-i
        return res1/res2


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        x = 1
        for i in xrange(max(m, n), m + n - 1):
            x *= i
        for i in xrange(2, min(m, n)):
            x /= i
        return x

