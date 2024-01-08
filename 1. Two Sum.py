class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Using HashMap
        PrevMap = { } 

        for i , n in enumerate(nums):
            diff = target - n
            if diff in PrevMap:
                return [PrevMap[diff],i]
            PrevMap[n] = i
        return
        
