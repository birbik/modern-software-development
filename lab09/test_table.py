# test_table.py — Автоматические проверки таблиц

from table import column_sums, diagonal_pattern, row_sums, transform

# 1. Прямоугольная матрица 2x3
matrix_2x3 = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix_2x3) == [6, 15]
assert column_sums(matrix_2x3) == [5, 7, 9]

# 2. Матрица 1x1
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# 3. Матрица-столбец 3x1
matrix_col = [[1], [-1], [0]]
assert row_sums(matrix_col) == [1, -1, 0]
assert column_sums(matrix_col) == [0]

# 4. Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# 5. Диагональный узор 3x3
expected_pattern_3 = [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]
assert diagonal_pattern(3) == expected_pattern_3

# Проверка независимости строк в узоре
pattern_copy_test = diagonal_pattern(3)
pattern_copy_test[0][0] = 99
assert pattern_copy_test[1][0] == 2
assert pattern_copy_test[2][0] == 2

# 6. Индивидуальный вариант 2: замена положительных на 1
sample_matrix = [[-2, 0, 3], [4, -5, 6]]
expected_transformed = [[-2, 0, 1], [1, -5, 1]]
result_transformed = transform(sample_matrix)
assert result_transformed == expected_transformed

# Проверка неизменяемости исходной матрицы при изменении результата
result_transformed[0][0] = 99
assert sample_matrix[0][0] == -2

print("Все проверки пройдены успешно!")
