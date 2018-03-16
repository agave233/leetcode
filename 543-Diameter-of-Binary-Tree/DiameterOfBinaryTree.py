# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diam = 0
        self.deepthOfSubTree(root)
        return self.diam
    
    def deepthOfSubTree(self, root):
        if root == None:
            return 0
        l_deepth, r_deepth = self.deepthOfSubTree(root.left), self.deepthOfSubTree(root.right)
        self.diam = max(self.diam, l_deepth + r_deepth)
        return max(l_deepth, r_deepth) + 1