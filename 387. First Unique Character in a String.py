class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for i in s:
            count[i] = count.get(i,0) + 1 

        for i , c in enumerate(s):
            if count[c] == 1:
                return i
        return -1 
 