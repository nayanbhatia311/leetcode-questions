class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0 or len(s)==1:
            return True
            
        leftpointer=0
        rightpointer=len(s)-1

        while leftpointer < rightpointer :
            while leftpointer<rightpointer and not s[leftpointer].isalnum():
                leftpointer+=1
            while leftpointer<rightpointer and not s[rightpointer].isalnum():
                rightpointer-=1
            
            if s[leftpointer].lower()!=s[rightpointer].lower():
                return False
            leftpointer+=1
            rightpointer-=1
        return True
