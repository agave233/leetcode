class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 重复值和越界值。
        nums.append(-1)
        for i in range(len(nums)):
            while nums[i] >= 0 and nums[i] != i:
                if nums[i] >= len(nums) or nums[i] == nums[nums[i]]:
                    nums[i] = -1
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                return i
        return len(nums)