class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res=[]

        for j in range(len(matrix[0])):
            temp=[]

            for i in range(len(matrix)):
                temp.append(matrix[i][j])

            res.append(temp)

        return res

