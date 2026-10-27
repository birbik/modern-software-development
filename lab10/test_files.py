# test_files.py — Автоматические проверки работы с файлами

import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import export_to_csv, read_matrix, selected_sum, write_report


def test_valid_reading():
    with TemporaryDirectory() as directory:
        # 1. Чтение матрицы 1x2
        p1 = Path(directory) / "m1.txt"
        p1.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(p1) == [[7, -1]]

        # 2. Чтение матрицы 1x1
        p2 = Path(directory) / "m2.txt"
        p2.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(p2) == [[0]]

        # 3. Чтение контрольной матрицы 2x3
        p3 = Path(directory) / "m3.txt"
        p3.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
        assert read_matrix(p3) == [[1, -2, 3], [4, 0, -6]]

        # 4. Чтение файла без завершающего \n
        p4 = Path(directory) / "m4.txt"
        p4.write_text("2 2\n1 2\n3 4", encoding="utf-8")
        assert read_matrix(p4) == [[1, 2], [3, 4]]


def test_invalid_formats():
    with TemporaryDirectory() as directory:
        # 1. Пустой файл
        p_empty = Path(directory) / "empty.txt"
        p_empty.write_text("", encoding="utf-8")
        try:
            read_matrix(p_empty)
            assert False, "Ошибка не обнаружена: пустой файл"
        except ValueError:
            pass

        # 2. Неверный заголовок: размер 0 3
        p_zero = Path(directory) / "zero.txt"
        p_zero.write_text("0 3\n", encoding="utf-8")
        try:
            read_matrix(p_zero)
            assert False, "Ошибка не обнаружена: размер 0"
        except ValueError:
            pass

        # 3. Недостаточно чисел в строке (ожидалось 2, дано 1)
        p_short = Path(directory) / "short.txt"
        p_short.write_text("1 2\n1\n", encoding="utf-8")
        try:
            read_matrix(p_short)
            assert False, "Ошибка не обнаружена: неполная строка"
        except ValueError as e:
            assert "Строка 2" in str(e)

        # 4. Нечисловое значение в строке данных
        p_char = Path(directory) / "char.txt"
        p_char.write_text("1 2\n1 x\n", encoding="utf-8")
        try:
            read_matrix(p_char)
            assert False, "Ошибка не обнаружена: нечисловая ячейка"
        except ValueError as e:
            assert "Строка 2" in str(e)

        # 5. Лишняя строка данных (заголовок 1 1, но 2 строки данных)
        p_extra = Path(directory) / "extra.txt"
        p_extra.write_text("1 1\n0\n1\n", encoding="utf-8")
        try:
            read_matrix(p_extra)
            assert False, "Ошибка не обнаружена: лишняя строка данных"
        except ValueError:
            pass

        # 6. Лишняя пустая строка в конце файла
        p_extra_nl = Path(directory) / "extra_nl.txt"
        p_extra_nl.write_text("1 1\n0\n\n", encoding="utf-8")
        try:
            read_matrix(p_extra_nl)
            assert False, "Ошибка не обнаружена: лишняя пустая строка в конце"
        except ValueError:
            pass

        # 7. Отсутствующий файл
        p_missing = Path(directory) / "missing.txt"
        try:
            read_matrix(p_missing)
            assert False, "Ошибка не обнаружена: файл отсутствует"
        except FileNotFoundError:
            pass


def test_selected_sum():
    # Вариант 2: Отрицательные элементы
    assert selected_sum([[1, -2, 3], [4, 0, -6]]) == -8
    assert selected_sum([[1, 2], [3, 4]]) == 0
    assert selected_sum([[-5, -10], [-1, -2]]) == -18
    assert selected_sum([]) == 0


def test_report_and_csv():
    with TemporaryDirectory() as directory:
        matrix = [[1, -2, 3], [4, 0, -6]]

        # Проверка записи отчета
        report_file = Path(directory) / "report.txt"
        write_report(report_file, matrix)
        content = report_file.read_text(encoding="utf-8")
        expected_content = (
            "Суммы строк: 2 -2\n"
            "Суммы столбцов: 5 -2 -3\n"
            "Результат варианта: -8\n"
        )
        assert content == expected_content

        # Проверка экспорта в CSV
        csv_file = Path(directory) / "matrix.csv"
        export_to_csv(csv_file, matrix)
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [list(map(int, r)) for r in reader]
        assert rows == matrix


def test_old_report_preserved_on_error():
    with TemporaryDirectory() as directory:
        report_file = Path(directory) / "report.txt"
        old_text = "ПРЕЖНЕЕ СОДЕРЖИМОЕ ОТЧЕТА"
        report_file.write_text(old_text, encoding="utf-8")

        bad_matrix_file = Path(directory) / "bad_matrix.txt"
        bad_matrix_file.write_text("1 2\n1 x\n", encoding="utf-8")

        # Имитируем логику main: при ошибке чтения матрицы запись отчета не выполняется
        try:
            _ = read_matrix(bad_matrix_file)
            write_report(report_file, _)
        except ValueError:
            pass

        # Проверяем, что report_file остался нетронутым
        assert report_file.read_text(encoding="utf-8") == old_text


if __name__ == "__main__":
    test_valid_reading()
    test_invalid_formats()
    test_selected_sum()
    test_report_and_csv()
    test_old_report_preserved_on_error()
    print("Все проверки пройдены успешно!")
