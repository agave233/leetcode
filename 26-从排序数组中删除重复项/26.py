class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                if i != k:
                    nums[k] = nums[i]
        return k + 1

# more concise
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in range(1,len(nums)):  
            if nums[i] != nums[k]:  
                k+=1  
                nums[k] = nums[i]  

        del nums[k+1:len(nums)]  
        return len(nums)  