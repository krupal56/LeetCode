class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashSet = {}
        for i in nums:
            hashSet[i] = 1 + hashSet.get(i,0)
        
        return max(hashSet, key=hashSet.get)