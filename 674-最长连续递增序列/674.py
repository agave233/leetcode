class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 忽略了[]的情况
        max_l, temp = 0, 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                temp += 1
            else:
                max_l = max(max_l, temp)
                temp = 1
        return max(max_l, temp) if nums else 0
    
       