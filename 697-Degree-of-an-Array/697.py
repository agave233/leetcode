class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, res = max(nums) + 1, len(nums)
        count = [0] * l
        
        for i in range(len(nums)):
            count[nums[i]] += 1
        degree = max(count)
        if degree == 1:
            return 1

        key = [i for i in range(l) if count[i] == degree]
        for each in key:
            a, b = -1, -1
            for i in range(len(nums)):
                if nums[i] == each:
                    b = i
                    if a == -1:
                        a = i
            res = min(res, b - a + 1)
        return res

# better
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        nodup = set(nums)

        left = {}
        right = {}
        count = {}

        for index,e in enumerate(nums):
            if e in count:
                count[e]+=1
                right[e] = index
            else:
                #不在
                count[e] = 1
                left[e] = index
                right[e] = index

        maxl = max(count.values())

        r = len(nums)
        for e in nodup:
            if count[e] == maxl:
                r = min(r,right[e]-left[e]+1)

        return r
        
# more pythonic
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)