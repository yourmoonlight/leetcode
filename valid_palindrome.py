class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        s2 = [i for i in s if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHI\
              JKLMNOPQRSTUVWXYZ0123456789"]
        s3 = ''.join(s2).lower()
        if len(s3) == 1 or len(s3) == 0:
            return True
        for j in range(len(s3)/2):
            if s3[j] != s3[len(s3) - 1 - j]:
                return False
        return True
