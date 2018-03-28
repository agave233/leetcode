class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, flag = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0 and flag == 0:
                k, flag = i, 1
            elif nums[i] and k != i and flag:
                nums[k], nums[i] = nums[i], 0
                k = k + 1

# easier
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j]=nums[i]
                j+=1
        for j in range(j,len(nums)):
            nums[j]=0

# more concise and pythonic
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)