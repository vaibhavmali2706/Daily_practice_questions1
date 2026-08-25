class Solution:
    def missingMultiple(self, nums,k) -> int:
        seen = set(nums)
        ans=k
        while ans in seen:
            ans+=k
            
        return ans