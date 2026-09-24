class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        indexi=-1    
        for i,j in enumerate(nums):
            sumi=0
            while(j>0):
                a=j%10
                sumi+=a
                j=j//10
                
            if i == sumi:
                
                indexi=i
                break
        return indexi
        
        