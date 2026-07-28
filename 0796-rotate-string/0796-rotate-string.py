class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        a=s+s
        return goal in a
        
        