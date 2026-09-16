class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        d=defaultdict(int)
        simple_str=''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        for word in simple_str.split():
            if word not in banned:
                d[word]+=1
        return max(d,key=d.get)