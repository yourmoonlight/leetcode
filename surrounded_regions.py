class Solution:
    # @param board, a 2D array
    # capture all regions by modifying the input board in-place
    # do not return any value
    def solve(self, board):
        def fill(x, y):
            if x > m - 1 or x < 0 or y > n - 1 or y < 0 or \
                    board[x][y] != "O":
                return
            queue.append((x, y))
            board[x][y] = "K"

        def bfs(x, y):
            if board[x][y] == "O":
                fill(x, y)
            while queue:
                cur = queue.pop()
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j - 1)
                fill(i, j + 1)
        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = []
        for i in xrange(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in xrange(1, m - 1):
            bfs(j, 0)
            bfs(j, n - 1)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "K":
                    board[i][j] = "O"
                elif board[i][j] == "O":  # pay attention elif not if!
                    board[i][j] = "X"
