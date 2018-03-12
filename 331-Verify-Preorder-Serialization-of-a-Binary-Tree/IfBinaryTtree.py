class Solution(object):
    
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        pre_list = preorder.split(',')
        n = len(pre_list)
        stack = []
        if pre_list == ['#']:
            return True
        if n < 3:
            return False
        stack.extend(pre_list[:2])

        for i in range(2,n):
            stack.append(pre_list[i])
            if stack[0] == '#':
                return False
            while stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                stack[-1] = '#'
                if len(stack) < 3: 
                    if len(stack) == 1 and i != n - 1:
                        return False
                    break
        
        return stack == ['#']