l = [1, 2, 1, 2, 3]


class Solution:
    # @param A, a list of integer
    # @return an integer
    def single_number(self, A):
        for i in A:
            if A.count(i) == 1:
                print i
    # single_number exceed time failed

    # use '^'
    def single_number2(self, A):
        answer = A[0]
        for i in range(1, len(A)):
            answer = answer ^ A[i]
        print answer

# s = Solution().single_number(l)

s2 = Solution().single_number2(l)
