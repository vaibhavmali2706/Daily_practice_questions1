class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = dict()
        for ch in s:
            if ch not in hmap:
                hmap[ch] = 1
            else:
                hmap[ch] += 1
        
        odd_count = 0
        for v in hmap.values():
            if v % 2 != 0:
                odd_count += 1
        
        if odd_count > 0:
            odd_count -= 1

        return sum(hmap.values()) - odd_count
