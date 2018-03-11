class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        x1 = 0
        x2 = 0
        Max = (height[0] if height[0] <= height[-1] else height[-1])*(len(height) - 1) 
        while(i < j):
            if height[i] < height[j]:
                
                if x1 < height[i]:
                    h = height[i] if height[i] <= height[j] else height[j]     
                    contain = h * (j - i)
                    if Max < contain:
                        Max = contain
                        x1 = height[i]
                i = i + 1

            elif height[i] > height[j]:
                
                if x2 < height[j]:
                    h = height[i] if height[i] <= height[j] else height[j]     
                    contain = h * (j - i)
                    if Max < contain:
                        Max = contain
                        x2 = height[j]
                j = j - 1
    
            else:
                h = height[i] if height[i] <= height[j] else height[j]     
                contain = h * (j - i)
                if Max < contain:
                    Max = contain
                    x1 = height[i]
                    x2 = height[j]
                i = i + 1
                j = j - 1
        return  Max