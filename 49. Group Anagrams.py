class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = defaultdict(list)
        
        for i in strs:
            sorted_array = sorted(i)
            if sorted_array in hashMap.values():
                hashMap[tuple(sorted_array)].append(i)
            else:
                hashMap[tuple(sorted_array)].append(i)
        return hashMap.values()


        