class Solution(object):
    def isPalindrome(self, s):
        ch=""
        for i in s.lower():
            if i.isalnum():
                ch+=i 
        return ch==ch[::-1]
        