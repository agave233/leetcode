class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = 0, len(numbers) - 1
        while index1 != index2:
            s = numbers[index1] + numbers[index2]
            if s < target:
                index1 += 1
            elif s > target:
                index2 -= 1
            else:
                return [index1 + 1, index2 + 1]

                