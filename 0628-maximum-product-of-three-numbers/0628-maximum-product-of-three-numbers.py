class Solution(object):
    def maximumProduct(self, nums):
        nums.sort(reverse=True)
        a=nums[0]*nums[1]*nums[2]
        b=nums[-1]*nums[-2]*nums[0]
        return max(a,b)
        