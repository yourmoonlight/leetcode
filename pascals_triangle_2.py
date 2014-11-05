class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        lists = [[] for i in range(rowIndex + 1)]
        # lists[0] = [1]
        lists[1] = [1, 1]
        for i in range(2, rowIndex + 1):
            lists[i] = [1 for j in range(i + 1)]
            for j in range(1, i):
                lists[i][j] == lists[i - 1][j - 1] + lists[i - 1][j]
        return lists[rowIndex]
