'''
reverse digits of an integer
example1: x = 123, return 321
example2: x = -123, return 321
'''


class Solution:
    # @return an integer
    def reverse(self, x):
        MAX_INT = 2147483647
        sign = 1 if x > 0 else -1
        x = abs(x)
        answer = 0
        while x > 0:
            answer = answer * 10 + x % 10
            x = x // 10
        if answer > MAX_INT:
            return 0
        else:
            return sign * answer
