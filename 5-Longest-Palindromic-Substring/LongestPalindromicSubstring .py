class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        tem = 0
        sub = ""
        i = 0
        l = len(s)
        for i in range(l-1):
            if (i < l-2) and (s[i] == s[i+2]):
                lx = 0
                tem = 1
                while i+1+tem <= l-2 and i+1-tem > 0:
                    tem = tem + 1
                    if s[i+1+tem] != s[i+1-tem]:
                        lx = -1
                        break             
                if len(sub) < (tem+lx)*2+1:
                    sub = s[i+1-tem-lx:i+tem+lx+2]
                    
            if s[i] == s[i+1]:
                lx = 0
                tem = 1
                while i+tem <= l-2 and i-tem+1 > 0:
                    tem = tem + 1
                    if s[i+tem] != s[i-tem+1]: 
                        lx = -1
                        break
                if len(sub) < (tem+lx)*2:
                    sub = s[i-tem-lx+1:i+tem+lx+1]
                
        return sub == "" and s[0] or sub