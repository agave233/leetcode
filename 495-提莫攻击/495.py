class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(duration, timeSeries[i] - timeSeries[i - 1])
        return res + duration
        