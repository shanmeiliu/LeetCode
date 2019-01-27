class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea =0
        n = len(height)
        i = 0
        j = n - 1
        while i <j:
            h=min(height[i],height[j])
            if maxarea < h*(j-i):
                maxarea=h*(j-i)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxarea
