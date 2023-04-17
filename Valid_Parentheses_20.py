class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        valid_brackets={'(': ')', '{' : '}', '[' : ']'}

        for bracket in s:
            if bracket in valid_brackets.keys():
                stack.append(bracket)
            elif bracket in valid_brackets.values():
                if len(stack)==0 or valid_brackets[stack.pop()]!=bracket:
                    return False
            else:
                return False

        if len(stack)==0:
            return True
        else:
            return False
