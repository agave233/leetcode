class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        start=0
        maxl=0
        for i in range(len(s)):
            
            if s[i] in d and start<=d[s[i]]:
                
                start=d[s[i]]+1
            d[s[i]]=i
            
            maxl=max(maxl,i-start+1)


        return maxl 