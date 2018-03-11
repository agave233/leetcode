class Solution(object):
    def reverse(self,x):
        """
        :typ+++++e x: int
        :rtype: int
        """
        if(x > 2147483647) | (x < -2147483647):
            return 0
        flag = 1
        l = []
        y = 0
        if x < 0:
            x = -x
            flag = -1
        while(x):
            l.append(x % 10)
            x = x / 10
        for i in range(len(l)):
            y = y * 10 + l[i]
        if(y > 2147483647) | (y < -2147483647):
            return 0
        return y*flag
            