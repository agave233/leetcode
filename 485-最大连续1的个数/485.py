class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len ,l= 0, 0
        for i in range(len(nums)):
            if nums[i]:
                l = l + 1
            if nums[i] == 0 and l:
                max_len, l = max(max_len, l), 0
                
        return max(l, max_len) 