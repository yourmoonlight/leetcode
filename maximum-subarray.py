class Solution:
    def max_subarray(self, A):
        # -max
        max_sum = float('-Inf')
        sum = 0
        for i in range(len(A)):
            sum = sum + A[i]
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum
