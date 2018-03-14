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
        cur_nodes = [root]
        mean_val = []
        
        while cur_nodes:
            temp_nodes = []
            sum = 0.0
            for node in cur_nodes:
                sum += node.val
                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)
            mean_val.append(sum / len(cur_nodes))
            cur_nodes = temp_nodes
            
        return mean_val