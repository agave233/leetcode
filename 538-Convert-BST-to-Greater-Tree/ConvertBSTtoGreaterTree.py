# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfsTree(root, 0)
        return root
    
    
    def dfsTree(self, root, add_val):
        if not root:
            return 0
        r_val = self.dfsTree(root.right, add_val)
        root.val += r_val if r_val else add_val 
        l_val = self.dfsTree(root.left, root.val)
        return l_val if l_val else root.val