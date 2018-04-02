class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        Ma = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                s = [M[i][j] for i in range(r-1,r+2) for j in range(c-1,c+2) if i >= 0 and i < m and j >= 0 and j < n]
                Ma[r][c] = sum(s) / len(s)
        return Ma
        