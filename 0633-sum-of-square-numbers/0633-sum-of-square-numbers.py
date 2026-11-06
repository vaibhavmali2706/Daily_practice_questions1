class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
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
            