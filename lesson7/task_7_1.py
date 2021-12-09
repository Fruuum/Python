class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(str, self.matrix))

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[0])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return "\n".join(map(str, new_matrix))


matrix1 = Matrix([[31, 22, -43, 5], [37, 43, 1, -3], [-22, 0, 51, 86]])
matrix2 = Matrix([[3, 5, 32, 0], [2, 4, 0, 6], [-1, 64, 12, -8]])
print(f"matrix1:\n{matrix1.__str__()}\nmatrix2:\n{matrix2.__str__()}\nsum_matrix:\n{matrix1 + matrix2}")
