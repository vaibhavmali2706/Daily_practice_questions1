class Solution:
    def finalString(self, s: str) -> str:
        sr=""
        for a in s:
            if a == "i" :
                sr=sr[::-1]
            else:
                sr+=a
                
        return sr
        