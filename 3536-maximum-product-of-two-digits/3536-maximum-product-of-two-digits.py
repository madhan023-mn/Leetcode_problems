class Solution(object):
    def maxProduct(self, n):
        l=sorted(str(n))
        return int(l[-1])*int(l[-2])     