# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

# 返回移除了所有不包含 1 的子树的原二叉树。

# ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

# 示例1:
# 输入: [1,null,0,0,1]
# 输出: [1,null,0,null,1]
 
# 解释: 
# 只有红色节点满足条件“所有不包含 1 的子树”。
# 右图为返回的答案。

# 示例2:
# 输入: [1,0,1,0,0,0,1]
# 输出: [1,null,1,null,1]

# 示例3:
# 输入: [1,1,0,1,1,0,1,0]
# 输出: [1,1,0,1,1,null,1]

# 说明:

# 给定的二叉树最多有 100 个节点。
# 每个节点的值只会为 0 或 1 

# ---------------------------------------------------------------------------------
# solution
# 二叉树深度优先搜索 + 回溯
# ---------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def deleteNode(root):
            if root == None:
                return True
            l, r = deleteNode(root.left), deleteNode(root.right)
            if l:
                root.left = None
            if r:
                root.right = None
            if l and r and root.val == 0:
                return True
            return False
            
        return root if deleteNode(root) == False else None