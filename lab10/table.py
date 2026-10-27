# table.py — Функции обработки таблиц и вложенных списков

def row_sums(matrix):
    """Возвращает список сумм строк матрицы. Для пустой матрицы возвращает []."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Возвращает список сумм столбцов прямоугольной матрицы. Для пустой матрицы возвращает []."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [sum(matrix[r][c] for r in range(rows)) for c in range(cols)]


def diagonal_pattern(size):
    """Создает квадратную таблицу: на главной диагонали 0, выше нее 1, ниже нее 2."""
    matrix = []
    for r in range(size):
        row = []
        for c in range(size):
            if r == c:
                row.append(0)
            elif r < c:
                row.append(1)
            else:
                row.append(2)
        matrix.append(row)
    return matrix


def transform(matrix):
    """Вариант 2: возвращает новую матрицу, где положительные числа заменены на 1."""
    if not matrix:
        return []
    new_matrix = []
    for row in matrix:
        new_row = [1 if val > 0 else val for val in row]
        new_matrix.append(new_row)
    return new_matrix
