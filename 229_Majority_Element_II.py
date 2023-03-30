class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter_dict={}
        output_list=[]
        for num in nums:
            if(counter_dict.get(num)):
                counter_dict[num]+=1
            else:
                counter_dict[num]=1
        for key,value in counter_dict.items():
            if value>len(nums)//3:
                output_list.append(key)

        return output_list
