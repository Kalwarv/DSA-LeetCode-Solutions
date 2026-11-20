class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        old = []

        for row in board:
            old.append(row.copy())

        for i in range(m):
            for j in range(n):

                count = 0

                if i > 0 and old[i-1][j] == 1:
                    count += 1

                if i < m-1 and old[i+1][j] == 1:
                    count += 1

                if j > 0 and old[i][j-1] == 1:
                    count += 1

                if j < n-1 and old[i][j+1] == 1:
                    count += 1

                if i > 0 and j > 0 and old[i-1][j-1] == 1:
                    count += 1

                if i > 0 and j < n-1 and old[i-1][j+1] == 1:
                    count += 1

                if i < m-1 and j > 0 and old[i+1][j-1] == 1:
                    count += 1

                if i < m-1 and j < n-1 and old[i+1][j+1] == 1:
                    count += 1

                if old[i][j] == 1:

                    if count < 2 or count > 3:
                        board[i][j] = 0

                else:

                    if count == 3:
                        board[i][j] = 1
