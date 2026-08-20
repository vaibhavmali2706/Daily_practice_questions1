class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        count=Counter(nums)
        for val in count.values():
            if val%2!=0:
                return False
        return True