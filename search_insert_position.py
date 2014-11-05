class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def search_insert(self, A, target):
        first = 0
        last = len(A) - 1
        while first <= last:
            mid = (first + last) // 2
            if A[mid] == target:
                return mid
            else:
                if target > A[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
        return first
