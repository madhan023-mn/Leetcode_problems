class Solution(object):
    def singleNumber(self, nums):
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i,j in f.items():
            if j==1:
                return i
        