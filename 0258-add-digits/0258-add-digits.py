class Solution(object):
    def addDigits(self, num):
        
        while num >= 10:
            s = 0
            
            while num > 0:
                d = num % 10
                s += d
                num //= 10
            
            num = s
            
        return num

        