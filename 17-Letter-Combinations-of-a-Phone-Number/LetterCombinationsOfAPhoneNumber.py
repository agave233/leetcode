class Solution(object):
       
    dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []
        return self.letterCom(digits,len(digits) - 1)
        
    def letterCom(self,digits,n):
        if n == 0:
            return self.dic[digits[0]]
        temp = self.letterCom(digits,n - 1)       
        current = [c + self.dic[digits[n]][0] for c in temp] + [c + self.dic[digits[n]][1] for c in temp] + [c + self.dic[digits[n]][2] for c in temp]
        if len(self.dic[digits[n]]) == 4:
            return current + [c + self.dic[digits[n]][3] for c in temp]
        return current