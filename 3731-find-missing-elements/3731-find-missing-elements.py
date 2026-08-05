class Solution(object):
    def findMissingElements(self, nums):
        i=min(nums)
        res=[]
        while i<=max(nums):
            if i not in nums:
                res.append(i)
            i+=1
        return res

            
        
        

        