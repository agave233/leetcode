class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return nums[0] if n else 0
        
        a, b = nums[0], nums[1] # a->not, b->have
        for i in range(2, n):
            temp = a
            a = max(a, b)
            b = temp + nums[i]
        
        return max(a, b)

# better
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = now = 0
        for num in nums:
            pre, now = now, max(pre + num, now)
        return now