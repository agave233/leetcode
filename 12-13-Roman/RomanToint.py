class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        SUM = 0
        for i in xrange(len(s) - 1):
            if L[s[i]] < L[s[i+1]]:
                SUM -= L[s[i]]
            else:
                SUM += L[s[i]]
        return SUM + L[s[-1]]