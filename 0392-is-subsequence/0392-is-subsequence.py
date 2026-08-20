class Solution(object):
    def isSubsequence(self, s, t):
        j=0
        for i in range(len(t)):
            if j<len(s):
                if t[i]==s[j]:
                    j+=1 
        return True if j==len(s) else False

        