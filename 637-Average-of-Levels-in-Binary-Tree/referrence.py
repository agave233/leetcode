# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # BFS
        if not root:
            return []
        ans = []        
        nodes = [root]
        while nodes:            
            ans.append(sum(node.val for node in nodes)/(len(nodes)+0.0))
            nodes = [x for node in nodes for x in (node.left, node.right)  if x]                            
        return ans