# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.collectTilt(root)[0]
    
    def collectTilt(self, root):
        if root == None:
            return 0, 0
        l, r = self.collectTilt(root.left), self.collectTilt(root.right)
        return l[0] + r[0] + abs(l[1] - r[1]), l[1] + r[1] + root.val