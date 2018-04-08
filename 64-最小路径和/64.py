class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid) - 1, len(grid[0]) - 1
        res = grid
        
        for i in range(r, -1, -1):
            res[i][c] += res[i + 1][c] if i != r else 0
            for j in range(c - 1, -1, -1):
                res[i][j] += min(res[i + 1][j], res[i][j + 1]) if i != r else res[i][j + 1]
        return res[0][0]