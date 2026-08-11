class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lprefix_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1 :
                lprefix_sum+=nums[i]
            else:
                break
        while lprefix_sum in nums :
            lprefix_sum+=1
        return lprefix_sum
        
        