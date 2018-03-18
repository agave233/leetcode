# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node.left:
                return node.val

            l, r = node.left.val, node.right.val
            if node.val == node.left.val:
                l = dfs(node.left)
            if node.val == node.right.val:
                r = dfs(node.right)

            return min(l, r) if node.val != l and node.val != r else max(l, r)
    
        res = dfs(root)
        return res if res != root.val else -1