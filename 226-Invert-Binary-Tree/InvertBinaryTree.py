# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.exchangeTree(root)
        return root
    
    def exchangeTree(self, root):
        if not root:
            return
        
        node = root.left
        root.left = root.right
        root.right = node
        
        self.exchangeTree(root.left)
        self.exchangeTree(root.right)