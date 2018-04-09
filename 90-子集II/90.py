class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for num in nums:
	        res += [each + [num] for each in res if each + [num] not in res]
        return res

#b 回溯思想
class Solution(object):
    def helper(self, ans, n, l, cur, pick):
        if l == n: return
        
        for i in range(len(pick)):
            if i == 0 or pick[i] != pick[i-1]:
                ret = cur + [pick[i]]
                ans.append(ret)
                self.helper(ans, n, l+1, ret, pick[i+1:])
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = [[]]
        self.helper(ans, len(nums), 0, [],nums)
        return ans
