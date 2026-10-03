class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res=[[0]*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i]=matrix[i][j]
        return res