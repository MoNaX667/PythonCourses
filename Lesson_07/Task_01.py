# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __add__(self, matrix_operand):
        sum_matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        for i in range(len(self.matrix_data)):

            for j in range(len(matrix_operand.matrix_data[i])):
                sum_matrix[i][j] = self.matrix_data[i][j] + matrix_operand.matrix_data[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in sum_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_data]))


# Script body
first_matrix = Matrix([[8, 1, 1],
                       [8, 7, 3],
                       [4, 2, 0]])

second_matrix = Matrix([[5, 2, 8],
                        [9, 1, 3],
                        [1, 0, 3]])

print(f"first_matrix:\n{first_matrix}")
print(f"second_matrix:\n{second_matrix}")

print(f"Sum of matrix:\n{first_matrix + second_matrix}")
