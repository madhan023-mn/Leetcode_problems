class Solution(object):
    def containsDuplicate(self, nums):
        a=set()
        b=[]
        for i in nums:
            if i in a:
                b.append(i)
            else:
                a.add(i)
        return len(nums)!=len(a)

        