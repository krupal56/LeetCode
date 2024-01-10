class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dictionary = {}
        for i in arr:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        count = len(dictionary)
        for j in sorted(dictionary.values()):
            k -= j
            if k < 0:
                return count
            else:
                count -= 1
        return count