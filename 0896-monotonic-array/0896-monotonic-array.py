class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def inc(nums):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
            return True

        def dec(nums):
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
            return True
        return dec(nums) or inc(nums)