class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        res=[""]*len(words)
        for word in words:
            pos=int(word[-1])
            a=word[:-1]
            res[pos-1]=a 
        return " ".join(res)
        
        