"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |

| -1 6 4 -8 |
| 3 5 8 3 |
| 8 3 7 1 |
"""
from pprint import pprint


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other_matrix):
        return Matrix(
            [[col + col_other
              for col, col_other in zip(row, row_other)]  # get col from row
             for row, row_other in zip(self.matrix, other_matrix)]  # get row from matrix
        )

    def __str__(self):
        return '\n'.join([str(row)
                         .replace('[', '|')
                         .replace(']', '|')
                          for row in self.matrix])



if __name__ == '__main__':
    m1 = [[2, 2],
          [2, 2],
          [2, 2]]

    m2 = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]

    mat_2_3 = Matrix(m1)
    mat_2_3 += m1
    print(mat_2_3)

    mat_3_3 = Matrix(m2)
    mat_3_3 += m2
    print(mat_3_3)
