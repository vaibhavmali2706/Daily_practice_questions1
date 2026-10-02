class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        if ord(x) > ord(y):
            return ''.join(sorted(s))
        else:
            return ''.join(sorted(s, reverse=True))