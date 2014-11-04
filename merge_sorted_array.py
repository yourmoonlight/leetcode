class Solution:
    # @param A a list of integers
    # @param m an integer, length of A
    # @param B a list of integers
    # @param n an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        temp = [0 for i in range(m+n)]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if A[i] < B[j]:
                temp[k] = A[i]
                i = i + 1
            else:
                temp[k] = B[j]
                j = j + 1
            k = k + 1

        if i == m:
            while k < m+n:
                temp[k] = B[j]
                j = j + 1
                k = k + 1
        else:
            while k < m+n:
                temp[k] = A[i]
                i = i + 1
                k = k + 1

        for i in range(0, len(temp)):
            A[i] = temp[i]
