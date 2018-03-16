# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        def dfs(root):
            if not root: return 0,0
            lsum, ltilt = dfs(root.left)
            rsum, rtilt = dfs(root.right)
            return root.val+lsum+rsum, abs(lsum-rsum)+ltilt+rtilt
        
        return dfs(root)[1]