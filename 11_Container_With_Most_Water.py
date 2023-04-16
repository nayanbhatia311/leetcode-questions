class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_soln=0
        leftpointer=0
        rightpointer=len(height)-1
        current_max=0
        while leftpointer<rightpointer:
            current_max=min(height[leftpointer],height[rightpointer])*(rightpointer-leftpointer)
            max_soln=max(max_soln,current_max)
            if height[leftpointer]>height[rightpointer]:
                rightpointer-=1
            else:
                leftpointer+=1 #confusion on how to decide
        return max_soln
