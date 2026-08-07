class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            digit=1
            temp=n
            while temp>0:
                digit*=temp%10
                temp//=10
            if digit%t ==0:
                return n
            n+=1

        