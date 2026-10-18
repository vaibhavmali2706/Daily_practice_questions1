class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target<nums[0]:
            return 0
        elif target>nums[len(nums)-1]:
            return len(nums)
        else:
            for i in range(0,len(nums)):
                if nums[i-1]<target<nums[i]:

                    return i