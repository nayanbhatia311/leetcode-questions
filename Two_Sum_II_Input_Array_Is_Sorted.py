class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #basically binary search after choicing one side can be one soln as well

        leftpointer=0
        rightpointer=len(nums)-1
        
        while leftpointer < rightpointer:
            temp_sum=nums[leftpointer]+nums[rightpointer]
            if temp_sum==target:
                return [leftpointer+1,rightpointer+1]

            elif temp_sum>target:
                rightpointer-=1
            else:
                leftpointer+=1

        return [-1,-1]
