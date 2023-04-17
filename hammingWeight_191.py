class Solution:
    def hammingWeight(self, n: int) -> int:
        total=0
        mask=1
        for _ in range(32):
            if mask & n != 0:
                total+=1
            mask <<=1
        


        return total
