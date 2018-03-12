# better solution:based on in-degree and out-degree


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """     
        diff=1
        for i in preorder.split(','):
            diff -= 1
            if diff<0:
                return False
            if i!='#':
                diff += 2
        return diff==0