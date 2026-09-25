class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        dic1={}
        dic2={}
        for i in words1:
            dic1[i]=dic1.get(i,0)+1
        for j in words2:
            dic2[j]=dic2.get(j,0)+1
        count=0
        for i in dic1:
            if dic1[i]==1 and i in dic2 and dic2[i]==1:
                count+=1
        return count
        
        