class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        L = [['','I','II','III','IV','V','VI','VII','VIII','IX']]
        L.append(['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'])
        L.append(['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'])
        L.append(['','M','MM','MMM'])
        A = ["","","",""]
        i = 0
        while num:
            A[i] = L[i][num % 10]
            num = (num - num % 10) / 10
            i = i + 1
        return A[3]+A[2]+A[1]+A[0]