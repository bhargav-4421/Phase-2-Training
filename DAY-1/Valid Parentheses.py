class Solution(object):
    def isValid(self,s):
        stack=[]
        for b in s:
            if b=="(":
                stack.append(")")
            elif b=="{":
                stack.append("}")
            elif b=="[":
                stack.append("]")
            elif len(stack)==0 or b!=stack.pop():
                return False
        return len(stack)==0
