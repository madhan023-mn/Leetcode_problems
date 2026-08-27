class Solution(object):
    def intersection(self, nums1, nums2):
        n=set(nums1)
        res=[]
        for i in nums2:
            if i in n:
                res.append(i)
                n.remove(i)
        return res
        

        