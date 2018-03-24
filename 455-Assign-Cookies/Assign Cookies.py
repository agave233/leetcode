class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        k, num, n = 0, 0, len(g)
        for each in s:
            if k == n:
                return num
            if each >= g[k]:
                k, num = k + 1, num + 1
        
        return num