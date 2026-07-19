class Solution(object):
    def isHappy(self, n):
        seen=[]
        while n!=1 and n not in seen:
            seen.append(n)
            s=0
            while n>0:
                d=n%10
                s+=d*d
                n//=10
            n=s 
        return n==1
        