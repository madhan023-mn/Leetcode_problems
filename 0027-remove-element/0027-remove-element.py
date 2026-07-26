class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in nums:
            if val!=i:
                nums[k]=i
                k+=1
        return k
        