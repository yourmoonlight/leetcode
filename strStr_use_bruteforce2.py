class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if haystack == "":
            return -1
        for startPos in range(len(haystack) - len(needle) + 1):
            matchLen = 0
            while haystack[startPos + matchLen] == needle[matchLen]:
                matchLen += 1
                if matchLen == len(needle):
                    return startPos
        else:
            return -1
