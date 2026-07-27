class Solution(object):
    def gcdOfOddEvenSums(self, n):
        even=2
        odd=1
        sum_odd=0
        sum_even=0
        for _ in range(n):
            sum_odd+=odd
            sum_even+=even
            odd+=2
            even+=2
        while sum_even!=0:
            sum_odd,sum_even=sum_even,sum_odd%sum_even
        gcd=sum_odd
        return gcd
        