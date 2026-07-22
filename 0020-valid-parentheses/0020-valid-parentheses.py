class Solution(object):
    def isValid(self, s):
        stack=[]
        is_vaild=True
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if ((i==']' and stack[-1]=='[') or (i=='}' and stack[-1]=='{' ) or (i==')' and stack[-1]=='(') ):
                        stack.pop() 
                    else:
                        is_vaild=False
                        break
                else:
                    is_vaild=False 
                    break
        if len(stack)!=0:
            is_vaild=False 
        return is_vaild
