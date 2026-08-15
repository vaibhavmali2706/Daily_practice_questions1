class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff=[]
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) == 2:
            i, j = diff
            if s[i] == goal[j] and s[j] == goal[i]:
                return True
        if len(diff)==0:
            hashmap = {}
            for c in s:
                hashmap[c] = hashmap.get(c, 0) + 1
            for freq in hashmap.values():
                if freq >= 2:
                    return True
        return False