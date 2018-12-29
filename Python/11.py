class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tmp = 0
        maxarea = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            tmp = self.calc(height, i, j)
            if (tmp > maxarea):
                maxarea = tmp
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return maxarea
    def calc(self, height, left,right):
        return  min(height[left], height[right]) * (right - left)

res = Solution()
height = [1,8,6,2,5,4,8,3,7]
area = res.maxArea(height)
print(area)