class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        e=""
        for i in t:
            if i in s:
                s=s.replace(i,"",1)
            else:
                e+=i
        return e
        