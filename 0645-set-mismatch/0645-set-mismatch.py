class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * (n + 1)
        for num in nums:
            counts[num] += 1

        missing = -1
        duple = -1
        for i in range(1, n + 1):
            if counts[i] > 1:
                duplicate = i
            elif counts[i] < 1:
                missing = i
                
        return duplicate, missing


        