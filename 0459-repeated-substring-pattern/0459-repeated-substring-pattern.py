class Solution(object):
    def repeatedSubstringPattern(self, s):
        double=s+s
        trim=double[1:-1]
        return s in trim
        