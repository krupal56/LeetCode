class Solution(object):
    def numberOfBeams(self, bank):
        sum = 0
        prev = bank[0].count('1')
        
        for i in range (1, len(bank)):
            curr = bank[i].count('1')
            if curr:
                sum += (curr * prev)
                prev = curr
        return sum

# Time Complexity O(n)
# Space Complexity O(1)