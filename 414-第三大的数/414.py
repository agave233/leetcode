class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = [float('-inf')] * 3
        for t in nums:
            if t > r[0] and t not in r:
                r[0] = t
                r.sort()
                
        return r[0] if r[0] > float('-inf') else r[2]

# another solution
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2= max3=None
        for num in nums:
            if num > max1:
                max2,max3 = max1,max2
                max1=num
            elif num > max2 and num < max1:
                max2,max3= num,max2
            elif num > max3 and num < max2:
                max3 = num
        return max1 if max3==None else max3

# O(nlgn)
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        n = len(nums)
        if n>=3:
            return nums[-3]
        else:
            return nums[-1]
