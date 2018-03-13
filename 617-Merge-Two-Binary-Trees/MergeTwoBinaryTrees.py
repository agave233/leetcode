# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        head = t1
        if not head:
            return t2
        self.searchTrees(t1, t2, None, None)
        return head

        
    def searchTrees(self, t1, t2, t1_parent, t2_parent):
        # t1 = None
        if not t1 and t2:
            if t2_parent.left == t2:
                t1_parent.left = t2
            else:
                t1_parent.right = t2
            return
        
        # t2 = None
        if not t2 and t1:
            self.searchTrees(t1.left, None, t1, t2)
            self.searchTrees(t1.right, None, t1, t2)
            
        # t1, t2 != None
        if t2 and t1:
            t1.val += t2.val
            self.searchTrees(t1.left, t2.left, t1, t2)
            self.searchTrees(t1.right, t2.right, t1, t2)