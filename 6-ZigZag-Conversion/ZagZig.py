def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        each = 2*numRows-2
        num = (len(s) / each + (len(s)%each and 1 or 0)) * each
        print num
        s1 = ""
        if numRows == 1:
            return s
        '''
        if numRows == 2:
            for i in range(0,num,2):
                s1 += s[i]
            for i in range(1,num,2):
                if i != len(s):
                    s1 += s[i]
            return s1
        '''
        k = 0
        for i in range(len(s)):
            if i%(num/each) == 0 and i:
                k += 1
            j = k % num
            print j,k
            if j < len(s):
                s1 += s[j]
                print s[j],
                print j
                t = j/each*each+each-j%each
                if j%each>0 and j%each<numRows-1 and t<len(s):
                    s1 += s[t]
                    print s1
            k = k + each
            if len(s1) == len(s):
                break
        return s1
print convert("PAYPALISHIRING",3)
