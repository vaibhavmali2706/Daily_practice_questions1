class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        ab=n
        while ab>0:
            d=ab%10
            s+=d
            p*=d
            ab//=10
        return n%(s+p)==0
        
        