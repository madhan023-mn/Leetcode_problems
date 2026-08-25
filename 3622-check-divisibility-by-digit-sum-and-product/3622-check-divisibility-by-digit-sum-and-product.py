class Solution(object):
    def checkDivisibility(self, n):
        s=0
        m=1
        temp=n
        while n>0:
            d=n%10 
            s+=d
            m*=d
            n//=10 
        total=s+m 
        if total!=0:
            return temp%total==0
        return False
        