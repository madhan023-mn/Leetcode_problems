class Solution(object):
    def tribonacci(self, n):
        a,b,c=0,1,1
        for i in range(1,n+1):
            a,b,c=b,c,a+b+c
        return a
        