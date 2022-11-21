class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        for index,num in enumerate(nums):
            sum+=num
            nums[index]=sum
            
        return nums
