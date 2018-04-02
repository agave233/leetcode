class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
	        res += [each + [num] for each in res]
        return res


# more pythonic
import itertools

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return sum((list(itertools.combinations(nums, n)) for n in xrange(len(nums) + 1)), [])