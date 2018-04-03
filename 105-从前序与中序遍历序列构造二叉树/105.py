# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            node = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            return node
        
# 非递归解法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not inorder or not preorder:
            return None

        f = []
        q = []
        t = None
        r = False
        m = {n: i for i, n in enumerate(inorder)}

        a, b = 0, len(inorder)
        x, y = 0, len(preorder)

        while True:
            if a < b and x < y:
                if not f:
                    p = t = TreeNode(preorder[x])
                elif not r:
                    p = f[-1].left = TreeNode(preorder[x])
                else:
                    p = f[-1].right = TreeNode(preorder[x])
                    f.pop()

                f.append(p)
                q.append((a, b, x, y))

                r = False
                b = m[preorder[x]]
                x = x + 1
                y = b - a + x
                
            elif not q:
                return t

            else:
                if r:
                    f.pop()
                    
                a, b, x, y = q.pop()
                a = m[preorder[x]] + 1
                x = y - b + a
                r = True