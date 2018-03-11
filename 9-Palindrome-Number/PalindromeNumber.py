class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
	        return False
        l = []
        while(x):
            l.append(x % 10)
            x = x / 10
        for i in range(len(l)/2):
	        if l[i] != l[len(l) - 1 -i]:
		        return False

        return True