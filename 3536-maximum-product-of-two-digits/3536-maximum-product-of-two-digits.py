class Solution(object):
    def maxProduct(self, n):
        l=[int(i) for i in str(n)]
        if len(l)<2:
            return 0
        l.sort(reverse=True)
        return l[0]*l[1]       