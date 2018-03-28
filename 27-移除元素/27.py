class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k, l, flag = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == val and flag == 0:
                k, flag = i, 1
            elif nums[i] != val:
                l += 1
                if k != i and flag:
                    nums[k], nums[i] = nums[i], 0
                    k += 1
        return l

# more concise
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)