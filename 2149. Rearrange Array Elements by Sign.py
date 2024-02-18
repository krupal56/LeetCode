class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res[l] = nums[i]
                l += 2
            if nums[i] < 0:
                res[r] = nums[i]
                r += 2    
            
            
        return res   
               
