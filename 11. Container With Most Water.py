class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] >= height[r]:
                Tarea = height[r] * (r-l)
                area = max(area,Tarea)
                r -= 1
            else:
                Tarea = height[l] * (r-l)
                area = max(area,Tarea)
                l += 1
        return area 
            

        