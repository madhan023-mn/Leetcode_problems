class Solution(object):
    def isPalindrome(self, x):
        temp=x
        s=0
        while x>0:
            d=x%10
            s=s*10+d
            x//=10
        return temp==s


        