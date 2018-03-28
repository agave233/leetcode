class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                nums[nums[i] - 1], nums[i] = nums[i], -1 if nums[nums[i] - 1] == nums[i] else nums[nums[i] - 1]

        return [i + 1 for i in range(len(nums)) if nums[i] == -1]

# more pythonic
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([num for num in range(1,len(nums) + 1)]) - set(nums))
