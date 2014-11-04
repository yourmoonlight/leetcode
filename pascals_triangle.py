class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 2]]
        if numRows > 2:
            lists = [[] for i in range(numRows)]
            for i in range(numRows):
                lists[i] = [1 for j in range(i + 1)]
            for i in range(2, numRows):
                for j in range(1, i):
                    lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
        return lists
