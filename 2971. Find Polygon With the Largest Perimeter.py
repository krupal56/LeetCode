class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = -1
        sum = 0

        for n in nums:
            if sum > n:
                res = sum + n
            sum += n

        return res





                

     

                      
            
