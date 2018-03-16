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
        ans = 0 
        if not root:
            return ans
        l = root.left
        r = root.right
        if l:
            if not l.left and not l.right:
                ans += l.val
            else:
                ans += self.sumOfLeftLeaves(l)
        if r:
            ans += self.sumOfLeftLeaves(r)
        return ans