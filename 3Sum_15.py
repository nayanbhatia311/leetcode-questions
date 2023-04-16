class Solution:
    def twoSum(self,soln, nums, thirdnumber):
        
        target_sum=[]
        leftpointer=0
        rightpointer=len(nums)-1

        while leftpointer < rightpointer:
            if nums[leftpointer]+nums[rightpointer]+thirdnumber==0:
                soln.append([nums[leftpointer],nums[rightpointer],thirdnumber])
                leftpointer+=1
                rightpointer-=1
                while leftpointer<rightpointer and nums[leftpointer]==nums[leftpointer-1]:
                    leftpointer+=1
                while leftpointer<rightpointer and nums[rightpointer]==nums[rightpointer+1]:
                    rightpointer-=1
            elif nums[leftpointer]+nums[rightpointer]+thirdnumber>0:
                rightpointer-=1
            else:
                leftpointer+=1
        

        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln=[]
        for index in range(len(nums)):
            if nums[index]>0:
                break
            if index==0 or nums[index-1]!=nums[index]: #since sorted, repeating the last value is what will cause duplicacy 
                temp=self.twoSum(soln,nums[index+1:],nums[index])
            

        return soln
