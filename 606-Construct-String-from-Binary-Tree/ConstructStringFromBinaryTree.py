# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ''
        # return str(t.val) + '(' + self.tree2str(t.left) + ')'\
        #                 + '(' + self.tree2str(t.right) + ')'
        
        s1, s2 = self.tree2str(t.left), self.tree2str(t.right)
        if s2:
            return str(t.val) + '(' + s1 + ')' + '(' + s2 + ')'
        
        if s1:
            return str(t.val) + '(' + s1 + ')'
        
        return str(t.val)