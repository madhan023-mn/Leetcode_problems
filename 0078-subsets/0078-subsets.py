class Solution(object):
    def subsets(self, nums):
        result=[[]]
        for i in nums:
            result+=[j+[i] for j in result]
        return result
        