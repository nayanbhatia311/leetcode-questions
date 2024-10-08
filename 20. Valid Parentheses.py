class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={'(':')','{':'}','[':']'}

        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)<1:
                    return False
                if dic.get(stack.pop())!=i:
                    
                    return False
        if len(stack)!=0:
            return False
        else:
            return True
            
