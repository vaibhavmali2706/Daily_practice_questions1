class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        else :
            l,r = 0,len(s)-1
            while l<r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else :
                    a = s
                    if r != len(a)-1:
                        a = a[:r]+a[r+1:]
                    else : 
                        a = a[:r]
                    if a == a[::-1]:
                        return True
                    s = s[:l]+s[l+1:]
                    if s == s[::-1]:
                        return True
                    else:
                        return False

        