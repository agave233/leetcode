class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mul, res, tag, n = 1, [], -1, len(nums)

        for i in range(n):
            if nums[i]:
                mul *= nums[i]
            elif tag == -1:
                tag = i
            else:
                return [0] * n

        if tag != -1:
            return [0] * tag + [mul] + [0] * (n - tag - 1)
        for each in nums:
            res.append(mul / each)
        return res

# more pythonic
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=nums.count(0)
        ans=[0]*len(nums)
        if x>1:
            return ans
        if x==1:
            product=reduce(lambda x,y:x if y==0 else y if x==0 else x*y,nums)
            ans[nums.index(0)]=product
            return ans
        product=reduce(lambda x,y:x*y,nums)
        ans=[product/i for i in nums]
        return ans