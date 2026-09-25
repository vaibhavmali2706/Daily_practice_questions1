class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        dic={}
        for i in list(s1.split()):
            dic[i]=dic.get(i,0)+1
        for j in list(s2.split()):
            dic[j]=dic.get(j,0)+1
        return [i for i in dic if dic[i]==1]
            

        