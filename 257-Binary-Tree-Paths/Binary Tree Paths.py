# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')
        
        res = []
        dfs(root, "")
        return res
            
            