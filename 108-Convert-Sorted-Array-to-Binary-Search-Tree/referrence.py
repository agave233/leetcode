# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left,right):
            if left > right:
                return None
            med = (left+right)/2
            new_node = TreeNode(nums[med])
            new_node.left = helper(left, med - 1)
            new_node.right = helper(med+1, right)
            return new_node
        
        return helper(0, len(nums)-1)