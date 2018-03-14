# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# s1
class Solution(object):
     def invertTree(self, root):
        if root is None:
            return root
        #swap lt and rt nodes
        root.left, root.right = root.right, root.left
        map(self.invertTree, (root.left, root.right))
        return root


# s2, 注意用回溯简化代码
class Solution():
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

