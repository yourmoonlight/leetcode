class Solution:
    def lengthOfLastWord(self, s):
        prelen = 0
        len = 0
        for i in s:
            if i == " ":
                if len != 0:
                    prelen = len
                    len = 0
                else:
                    pass
            else:
                len = len + 1
        if len == 0:
            return prelen
        else:
            return len
