class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        l = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[n]
