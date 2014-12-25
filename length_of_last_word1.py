class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        len = 0
        for letter in s:
            if letter == " ":
                len = 0
            else:
                len = len + 1
        return len
