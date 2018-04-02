class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n, i = len(digits), 0
        while digits[n - i -1] == 9 and i < n:
            i += 1
        if i == n:
            digits = [1]
        else:
            digits[n - i -1] += 1
            digits = digits[0:n - i]
        digits.extend([0] * i)
        return digits