# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
                """
        m, n, res = len(A), len(B), 0
        if m > n:
            A, B = B, A
            m, n = n, m
        i, j = 0, 0

        for k in range(1, m + n):
            if k < m:
                a, b = A[m - k:], B[:k] 
            else:
                a, b = A[:m + n - k], B[k - m:k]
            c = ['0' if i == j else '1' for i, j in zip(a, b)]
            d = ''.join(c).split('1')
            res = max(res, max([len(s) for s in d]))
        return res



class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lengthA = len(A)
        result = 0
        temp = [0]*(lengthA+1)
        for b in B:
            temp2 = [0]
            for index in range(lengthA):
                if b==A[index]:
                    temp2.append(temp[index]+1)
                else:
                    temp2.append(0)
            #print temp2
            result = max(result,max(temp2))
            temp = temp2
        return result