# 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到并返回最大的集合S，S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

# 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

# 示例 1:

# 输入: A = [5,4,0,3,1,6,2]
# 输出: 4
# 解释: 
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

# 其中一种最长的 S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# 注意:

# N是[1, 20,000]之间的整数。
# A中不含有重复的元素。
# A中的元素大小在[0, N-1]之间。

# ------------------------------------------------------------------------------------------------------------------------
# soulution
# 每次从一个元素开始进行嵌套的迭代搜索，并且所有访问过的元素用一个hash表记录。还需一个变量来指示去进行嵌套迭代的起始点（以便一个group
# 找完之后能够回到离开的index继续搜索），这样每一个元素至多被访问3次。
# 需要O(n)的时间复杂度和O(n)的空间复杂度
# ------------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [0] * len(nums)
        res = 0
        k, l, t, m = 0, 0, 0, 0
        while l != len(nums):
            if visited[k] == 0:
                t, l = t + 1, l + 1
                visited[k] = 1
                k = nums[k]
            else:
                res = max(res, t)
                m = m + 1
                k, t = m, 0
            
        return max(res, t)


# another solution
# 用栈的方法
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for i in range(len(nums)):
            dic[i] = nums[i]
        se = set(nums)
        res = 0
        while len(se) > 0:
            se1 = 1
            start = se.pop()
            p = nums[start]
            while p != start:
                se.remove(p)
                p = nums[p]
                se1 += 1
            res = res < se1 and se1 or res
        return res