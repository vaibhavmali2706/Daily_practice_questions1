class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tar=0
        for i in range(0,len(nums)):
            for j in range(i, len(nums)):
                sub=nums[i:j+1]
                r=len(set(sub))
                tar+=r*r
        return tar