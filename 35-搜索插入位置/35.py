class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, mid, end = 0, 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return start

# another solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pre = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                pre += 1
        return pre    
