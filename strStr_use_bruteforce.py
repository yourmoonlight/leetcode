class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) == "":
            return -1
        if len(needle) == "":
            return 0

        begin = 0
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        while lenHaystack - begin >= lenNeedle:
            for index in range(0, lenNeedle):
                if haystack[begin + index] != needle[index]:
                    break
            else:
                return begin
            begin = begin + 1
        return -1
