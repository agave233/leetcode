# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q:
            temp = []
            check = []
            for each in q:
                if not each:
                    check.append('')
                else:
                    check.append(each.val)
                    temp.extend([each.left, each.right])
            q = temp
            if check != check[::-1]:
                return False
        return True