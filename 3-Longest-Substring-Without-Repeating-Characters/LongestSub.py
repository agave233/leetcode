class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = []
        l_max = 0
        l_sub = 0
        l_str = len(s)
        for i in range(l_str):
            if s[i] not in sub:
                sub.append(s[i])
            else:
                l_sub = len(sub)
                if l_max < l_sub:
                    l_max = l_sub
                k = sub.index(s[i])
                if sub[-1] != s[i]:
                    sub = sub[k + 1:]
                else:
                    sub = []
                sub.append(s[i])
        if l_max < len(sub):
            return len(sub)
        else:
            return l_max