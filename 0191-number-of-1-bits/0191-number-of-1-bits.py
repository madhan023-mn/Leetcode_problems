class Solution(object):
    def hammingWeight(self, n):
        a=bin(n)[2:]
        c=0
        for i in a:
            if '1' in i:
                c+=1
        return c
        