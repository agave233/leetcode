class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[-1] # 必须初始化定义
        while len(nums) > 1:
            nums = [nums[i] for i in range(0, len(nums) - 1, 2) if nums[i] == nums[i + 1]]
            if len(nums) % 2:
                res = nums[-1]
        # return res if nums == None else nums[-1] # 会报错
        return nums[0] if nums else res


# more concise
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]