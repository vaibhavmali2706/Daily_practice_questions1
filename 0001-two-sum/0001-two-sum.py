class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for current in range(len(nums)):
            needed = target - nums[current]
            if needed in seen:
                return [seen[needed],current]

            seen[nums[current]] = current
