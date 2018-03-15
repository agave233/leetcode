class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        Common = ""
        erro = 0
        for i in xrange(len(strs[0])):
            tmp = strs[0][i]
            for j in xrange(1,len(strs)):
                try:
                    if strs[j][i] != tmp:
                        erro = 1
                        break
                except:
                    erro = 1
                    break
            if erro:
                break
            Common += tmp
        return Common