class Solution:
    def countElements(self, nums: list[int]) -> int:
        cnt = 0
        min_= min(nums)
        max_ = max(nums)
        for i in nums:
            if i > min_ and i < max_:
                cnt += 1
        return cnt
        