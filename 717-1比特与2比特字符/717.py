class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        k, tmp = 0, 0
        while k < len(bits):
            tmp, k = k, k + 1 if bits[k] == 0 else k + 2
        return False if bits[tmp] else True

# another solution
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits: return False
        n = len(bits)

        index = 0
        while index < n:
            if index == n-1 : return True
            if bits[index] == 1: 
                index += 2              
            else: index += 1
        return False