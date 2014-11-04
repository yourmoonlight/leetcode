class Solution:
    # @param A a list of integers
    # @param elem an integer, value need to be removed
    # @return an integer
    def remove_element(self, A, elem):
        while elem in A:
            A.pop(A.index(elem))
        return len(A)
