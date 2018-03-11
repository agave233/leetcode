class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        
        n, step, ret = len(s), 2*numRows - 2, ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                ret += s[i:n:step]
                continue
            
            j, k = i, step - i
            while j < n:
                ret += s[j]
                j += step

                if k < n:
                    ret += s[k]
                    k += step
                            
        return ret

'''
coding style!
'''