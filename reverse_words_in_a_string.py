'''
given s = "the sky is blue"
return "blue is sky the"
'''


class Solution:
    # @param s, a string
    # @return a string
    def reverse_words(self, s):
        return " ".join(s.split()[::-1])
