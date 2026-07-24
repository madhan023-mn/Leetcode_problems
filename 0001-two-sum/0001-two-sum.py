class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff not in d:
                d[nums[i]]=i
            else:
                return d[diff],i
        