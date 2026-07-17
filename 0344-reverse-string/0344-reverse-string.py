class Solution(object):
    def reverseString(self, s):
        ch=[]
        for i in range(len(s)-1,-1,-1):
            ch.append(s[i])
        for i in range(len(s)):
            s[i] = ch[i]
        
        