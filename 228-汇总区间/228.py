class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
	        return []
        res, l, n = [], 0, len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                res += [str(nums[l])] if l == i - 1 else [str(nums[l]) + '->' + str(nums[i - 1])]
                l = i

        return res + [str(nums[l])] if l == n - 1 else res + [str(nums[l]) + '->' + str(nums[n - 1])]

# other solution
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        nums += [nums[0] - 1]
        res = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            if i == j + 1:
                res += [str(nums[j])]
                j = i
            else:
                res += [str(nums[j])+'->'+str(nums[i-1])]
                j = i
        return res