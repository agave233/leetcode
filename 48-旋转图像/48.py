class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n / 2):
            top = matrix[i][i:n - i]
            bottom = matrix[n - 1 - i][i:n - i]
            left = [matrix[j][i] for j in range(i, n - i)]
            right = [matrix[j][n - 1 - i] for j in range(i, n - i)]

            for j in range(i, n - i):
                matrix[j][i] = bottom[j - i]
                matrix[j][n - 1 - i] = top[j - i]
            matrix[i][i:n - i] = left[::-1];
            matrix[n - 1 - i][i:n - i] = right[::-1]

# more concise
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        matrixx=[]
        for i in range(n):
            matrixx.append([])
            for j in range(n):
                matrixx[i].append(None)
        for i in range(n):
            for j in range(n):
                matrixx[j][n-i-1]=matrix[i][j]
        matrix[:]=matrixx[:]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        
        for i in range(l-1):
            for j in range(i+1,l):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        if l == 1:
            pass
        else:
            for i in range(l):
                matrix[i]=matrix[i][::-1]