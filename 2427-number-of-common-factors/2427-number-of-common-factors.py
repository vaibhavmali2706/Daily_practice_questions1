class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cnt=0
        for i in range(b+1):
            if i==0:
                pass
            elif a%i ==0 and b%i ==0:
                cnt+=1
        return cnt