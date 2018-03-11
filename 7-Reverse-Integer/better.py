class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sx = str(x)
        if '-' in sx:
            value = -int(sx[1:][::-1])
        else:
            value = int(sx[::-1])
        return 0 if value > 2147483647 or value < -2147483647 else value