class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digip(n):
            x=1
            while n>0:
                a=n%10
                x *= a
                n //= 10
            return x
        while True:
            if digip(n)%t==0:
                return(n)
                break
            n+=1