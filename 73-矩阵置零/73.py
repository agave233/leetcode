# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:

# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:

# 输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:

# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n, r, c = '#', len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][:] = [0 if matrix[i][k] == 0 else n for k in range(c)]
                    for k in range(r):
                        matrix[k][j] = 0 if matrix[k][j] == 0 else n

        #matrix = [[0 if matrix[i][j] == n else matrix[i][j] for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = 0 if matrix[i][j] == n else matrix[i][j]


class Solution(object):
    def setZeroes(self, matrix):
        
        m = len(matrix)
        n = len(matrix[0])
        
        if m*n !=0:
            
            row = 0
            col = 0

            for i in range(m):
                for j in range(n):
                    if matrix[i][j] ==0:
                        row = row | (1<<i)
                        col = col | (1<<j)
            i=0
            while row !=0:
                if row & 1 !=0:
                    for k in range(n):
                        matrix[i][k] =0
                row = row>>1
                i +=1
            j=0
            while col !=0:
                if col & 1 !=0:
                    for k in range(m):
                        matrix[k][j] =0
                col = col>>1
                j+=1

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowSet = set()
        colSet = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        for r in rowSet:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in colSet:
            for r in range(len(matrix)):
                matrix[r][c] = 0

