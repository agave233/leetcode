# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        node = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        
        node.left = self.buildTree(inorder[:mid], postorder[:mid])
        node.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return node