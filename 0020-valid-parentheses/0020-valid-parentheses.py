class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # Opening brackets
            if ch in "({[":
                stack.append(ch)

            # Closing brackets
            else:
                # Stack empty OR top doesn't match
                if not stack or stack[-1] !=mapping[ch]:
                    return False

                stack.pop()

        return len(stack) == 0
        