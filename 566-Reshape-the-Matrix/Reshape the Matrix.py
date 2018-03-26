class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r0, c0 = len(nums), len(nums[0])
        if c0 * r0 != c * r:
            return nums
        k, l, res = 0, 0, []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[k][l])
                if l == c0 - 1:
                    k = k + 1
                    l = 0
                else:
                    l = l + 1
            res.append(temp)
        return res

# more pythonic

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        N=sum(nums,[])
        if len(N) != r*c:
            return nums
        return [N[i:i + c] for i in range(0, len(N), c)]