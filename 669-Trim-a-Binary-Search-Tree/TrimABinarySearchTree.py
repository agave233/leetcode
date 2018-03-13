# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return self.deleteTree(root, root, None, L, R)
    
    def deleteTree(self, head, node, parent, L, R):
        if node == None:
            return head
  
        if node.val < L:
            if parent == None:
                return self.deleteTree(node.right, node.right, None, L, R)
            else:
                if parent.right == node:
                    parent.right = node.right
                else:
                    parent.left = node.right
                return self.deleteTree(head, node.right, parent, L, R)
                
        elif node.val > R:
            if parent == None:
                return self.deleteTree(node.left, node.left, None, L, R)
            else:
                if parent.right == node:
                    parent.right = node.left
                else:
                    parent.left = node.left 
                return self.deleteTree(head, node.left, parent, L, R)
                
        
        head = self.deleteTree(head, node.left, node, L, R)
        return self.deleteTree(head, node.right, node, L, R)