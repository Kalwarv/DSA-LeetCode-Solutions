class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        result = []

        i = 0
        j = 0

        up = True

        for k in range(m * n):

            result.append(mat[i][j])

            if up:

                if j == n - 1:
                    i += 1
                    up = False

                elif i == 0:
                    j += 1
                    up = False

                else:
                    i -= 1
                    j += 1

            else:

                if i == m - 1:
                    j += 1
                    up = True

                elif j == 0:
                    i += 1
                    up = True

                else:
                    i += 1
                    j -= 1

        return result
