class Solution:
    # @return a string
    def longestPalindrome(self, s):
        palindrome = ''
        for i in xrange(len(s)):
            palindrome1 = self.getLongestPalindrome(s, i, i)
            len1 = len(palindrome1)
            if len1 > len(palindrome):
                palindrome = palindrome1
            palindrome2 = self.getLongestPalindrome(s, i, i+1)
            len2 = len(palindrome2)
            if len2 > len(palindrome):
                palindrome = palindrome2
        return palindrome

    def getLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
