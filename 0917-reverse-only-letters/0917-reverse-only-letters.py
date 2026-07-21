class Solution(object):
    def reverseOnlyLetters(self, s):
        ch=""
        for i in s:
            if i.isalpha():
                ch=i+ch
        ans=""
        k=0
        for i in s:
            if i.isalpha():
                ans+=ch[k]
                k+=1
            else:
                ans+=i
        return ans
        