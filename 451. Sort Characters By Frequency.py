class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        bucket = defaultdict(list)
        
        for char , n in count.items():
            bucket[n].append(char)

        res = ""
        for i in range(len(s),0,-1):
            for c in bucket[i]:
                res += c * i
        return res
            