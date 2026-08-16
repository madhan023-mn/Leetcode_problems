class Solution(object):
    def getMinDistance(self, nums, target, start):
        s=float('inf')
        for i in range(len(nums)):
            if target==nums[i]:
                s=min(s,abs(i-start))
        return s
                
        