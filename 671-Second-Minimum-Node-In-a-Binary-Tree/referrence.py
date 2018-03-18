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
        if not root.left and not root.right:
            return -1
        if root.val < root.left.val:
            l = root.left.val
        else:
            l = self.findSecondMinimumValue(root.left)
        if root.val < root.right.val:
            r = root.right.val
        else:
            r = self.findSecondMinimumValue(root.right)
        if l == -1:
            return r
        if r == -1:
            return l
        return min(l, r)

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        cur = root
        val = []
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            if stack == []:
                break
            cur = stack.pop()
            val.append(cur.val)
            cur = cur.right
        secm, min_m = float('inf'), root.val
        for i in range(0, len(val)):
            if val[i] < secm and val[i] != min_m:
                
                secm = val[i]
        
        return secm if secm < float('inf') else -1

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min1, self.min2 = root.val, float('infinity')
        
        def preOrder(root):
            if root:
                if self.min2 > root.val > self.min1:
                    self.min2 = root.val
                    # no need to search subtree further
                else:
                    preOrder(root.left)
                    preOrder(root.right)    
        preOrder(root)
        return self.min2 if self.min2 < float('infinity') else -1
