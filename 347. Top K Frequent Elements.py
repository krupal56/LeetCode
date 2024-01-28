
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = [(freq,value) for (value,freq) in counter.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [value for (freq,value) in heap]