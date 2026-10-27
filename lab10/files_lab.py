# files_lab.py — Чтение матриц из файлов и запись отчетов

import csv
from pathlib import Path
from table import column_sums, row_sums


def read_matrix(path):
    """Читает прямоугольную матрицу целых чисел из файла формата UTF-8.
    
    Первая строка файла содержит количество строк и столбцов.
    Последующие строки содержат элементы матрицы.
    При нарушении формата возбуждает ValueError с указанием причины.
    """
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Проверка на пустой файл
    if not content:
        raise ValueError("Файл пуст")

    # Нормализация переводов строк
    content = content.replace("\r\n", "\n").replace("\r", "\n")

    # Допустим один завершающий перевод строки в конце файла
    if content.endswith("\n"):
        content = content[:-1]

    # Если после удаления одного перевода строки остался перевод строки — это лишняя пустая строка
    if content.endswith("\n"):
        raise ValueError("Обнаружена лишняя пустая строка в конце файла")

    lines = content.split("\n")

    # Проверка заголовка (строка 1)
    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: заголовок должен содержать ровно 2 числа (строки и столбцы)")

    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError(f"Строка 1: заголовок содержит нечисловое значение '{lines[0]}'")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше 0")

    # Проверка количества строк данных
    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Неверное количество строк данных: ожидалось {rows}, получено {len(data_lines)}")

    matrix = []
    for idx, line in enumerate(data_lines, start=2):
        if not line.strip():
            raise ValueError(f"Строка {idx}: пустая строка недопустима")

        parts = line.split()
        if len(parts) != cols:
            raise ValueError(f"Строка {idx}: ожидалось {cols} чисел, получено {len(parts)}")

        row = []
        for p in parts:
            try:
                row.append(int(p))
            except ValueError:
                raise ValueError(f"Строка {idx}: значение '{p}' не является целым числом")
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    """Вариант 2: возвращает сумму отрицательных элементов матрицы (или 0 при их отсутствии)."""
    return sum(val for row in matrix for val in row if val < 0)


def write_report(path, matrix):
    """Формирует и записывает отчет по матрице в файл в кодировке UTF-8."""
    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    v_sum = selected_sum(matrix)

    r_str = " ".join(str(x) for x in r_sums)
    c_str = " ".join(str(x) for x in c_sums)

    report_content = (
        f"Суммы строк: {r_str}\n"
        f"Суммы столбцов: {c_str}\n"
        f"Результат варианта: {v_sum}\n"
    )

    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report_content)


def export_to_csv(path, matrix):
    """Экспортирует матрицу в CSV файл с помощью стандартного модуля csv."""
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)
