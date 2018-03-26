class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[2 * i] for i in range(len(nums) / 2)])

        # solution2:more pythonic
        return sum(sorted(nums)[::2])