class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        bar = False
        for char in s:
            if char == '|':
                bar = not bar
            elif char == '*' and not bar:
                count += 1
        return count
    
