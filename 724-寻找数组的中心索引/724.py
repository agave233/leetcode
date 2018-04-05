class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum1, sum2 = 0, sum(nums[1:])
        
        for i in range(len(nums) - 1):
            if sum1 == sum2:
                return i
            sum1, sum2 = sum1 + nums[i], sum2 - nums[i + 1]
                
        return len(nums) - 1 if sum1 == 0 else -1


# more pythonic
class Solution(object):
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1