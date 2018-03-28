class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def AreaOfIsland(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or flag[i][j] == 1 or grid[i][j] == 0:
                return 0
            flag[i][j] = 1
            return 1 + AreaOfIsland(i + 1, j) + AreaOfIsland(i, j + 1) + AreaOfIsland(i - 1, j) + AreaOfIsland(i, j - 1)
            
        r, c, max_area = len(grid), len(grid[0]), 0
        flag = [ [0] * c for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                if flag[i][j] == 0 and grid[i][j] == 1:
                    max_area = max(max_area, AreaOfIsland(i, j))
        return max_area

# more concise
class Solution(object):
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0