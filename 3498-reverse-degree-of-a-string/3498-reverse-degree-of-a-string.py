class Solution:
    def reverseDegree(self, s: str) -> int:
        tar=0
        j=1
        for i in s:

            tar+=(123-ord(i))*j
            j+=1
        return tar