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
        if not nums:
            return None
        l = len(nums) / 2
        root = TreeNode(nums[l])
        root.left, root.right = self.sortedArrayToBST(nums[:l]), self.sortedArrayToBST(nums[(l + 1):])
        return root
    