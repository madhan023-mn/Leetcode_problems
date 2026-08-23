class Solution(object):
    def thirdMax(self, nums):
        s=t=l=float('-inf')
        for i in nums:
            if i == l or i == s or i == t:
                continue
            if i > l :
                t=s
                s=l 
                l=i 
            elif i > s:
                t=s
                s=i 
            elif i > t:
                t=i 
        if t==float('-inf'):
            return l
        return t
            
        