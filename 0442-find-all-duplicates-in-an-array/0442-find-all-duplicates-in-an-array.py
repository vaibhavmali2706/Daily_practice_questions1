class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num, freq in hashmap.items():
            if freq > 1:
                result.append(num)
        return result