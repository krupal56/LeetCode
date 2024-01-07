class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        list = [ ]
        try:
            for i in range(1,n+1):
                if n%i==0:
                    list.append(i)
            return list[k-1]
        except:
            return -1