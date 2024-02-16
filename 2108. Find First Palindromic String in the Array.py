class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for s in words:
            l, r = 0, len(s) - 1
            while s[l] == s[r]:
                if l >=r :
                    return s
                l, r = l + 1, r - 1 
        return ""
        