class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(math.sqrt(c))
        while (i<=j):
            r = i*i + j*j 
            if r == c:
                return True
            elif r < c :
                i+=1
            else:
                j-=1
        return False
            