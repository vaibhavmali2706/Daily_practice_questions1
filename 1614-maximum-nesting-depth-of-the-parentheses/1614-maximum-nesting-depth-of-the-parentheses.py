class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        max_w=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
                max_w=max(max_w,len(stack))
            elif s[i]==')':
                stack.pop()
        return max_w
        