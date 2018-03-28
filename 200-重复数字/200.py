class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != -1:
                if nums[i] == len(nums):
                    nums[i] = -1
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

# more concise
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)