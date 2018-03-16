# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.visitLeftLeaves(root, root)
    
    def visitLeftLeaves(self, root, par):
        if root == None:
            return 0
        # if root == par.left and l == 0 and r == 0:
        #    return root.val
        if root == par.left and root.left == None and root.right == None:
            return root.val
        return self.visitLeftLeaves(root.left, root) + self.visitLeftLeaves(root.right, root)