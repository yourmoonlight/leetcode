class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        '''
        Could negative integers be palindromes? (ie, -1)

        If you are thinking of converting the integer to string, note the
        restriction of using extra space.

        You could also try reversing an integer. However, if you have

        solved the problem "Reverse Integer", you know that the reversed

        integer might overflow. How would you handle such case?

        There is a more generic way of solving this problem.
        '''
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
        while x:
            left = x / div
            right = x % 10
            if left != right:
                return False
            x = (x % div) / 10
            div = div / 100
        return True
