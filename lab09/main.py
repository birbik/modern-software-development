# main.py — Ввод и обработка прямоугольной таблицы

from table import column_sums, diagonal_pattern, row_sums, transform


def print_matrix(matrix):
    """Выводит матрицу построчно с пробелами между числами."""
    for row in matrix:
        print(*row)


def main():
    # 1. Ввод прямоугольной таблицы с проверкой длины строк
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))

    matrix = []
    for i in range(rows):
        row = [int(part) for part in input(f"Строка {i + 1} таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input(f"Повторите строку {i + 1}: ").split()]
        matrix.append(row)

    print("\nИсходная таблица:")
    print_matrix(matrix)

    # 2. Вычисление сумм строк и столбцов
    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    print(f"\nСуммы строк: {r_sums}")
    print(f"Суммы столбцов: {c_sums}")

    # 3. Преобразование по индивидуальному варианту 2
    transformed = transform(matrix)
    print("\nПреобразованная таблица (положительные заменены на 1):")
    print_matrix(transformed)

    # 4. Диагональный узор
    size = int(input("\nВведите размер квадратного узора: "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    print_matrix(pattern)


if __name__ == "__main__":
    main()
