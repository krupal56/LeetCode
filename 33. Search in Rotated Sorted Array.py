class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target:
                return m
            else:
                if target < nums[l] and nums[l] < nums[m]:
                    l = m + 1
                else:
                    r = r - 1 
        return -1
