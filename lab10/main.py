# main.py — Главная программа обработки файлов матриц

from pathlib import Path
from files_lab import export_to_csv, read_matrix, write_report


def read_positive_integer(prompt="Введите размер (целое число > 0): "):
    """Запрашивает у пользователя целое положительное число с обработкой ошибок ввода."""
    while True:
        raw = input(prompt)
        try:
            val = int(raw)
        except ValueError:
            print("Ошибка: не целое число")
            continue
        if val <= 0:
            print("Ошибка: должно быть больше нуля")
            continue
        return val


def main():
    print("--- 1. Демонстрация надежного ввода размера ---")
    size = read_positive_integer("Введите положительное целое число: ")
    print(f"Принято число: {size}\n")

    print("--- 2. Чтение матрицы и формирование отчета ---")
    folder = Path(__file__).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"
    csv_path = folder / "matrix.csv"

    # Чтение матрицы с перехватом всех возможных ошибок
    try:
        matrix = read_matrix(matrix_path)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден ({matrix_path})")
        return
    except UnicodeDecodeError:
        print(f"Ошибка: неверная кодировка файла ({matrix_path}), требуется UTF-8")
        return
    except ValueError as err:
        print(f"Ошибка формата данных: {err}")
        return
    except OSError as err:
        print(f"Системная ошибка доступа при чтении файла: {err}")
        return

    # Запись отчета выполняется только после успешной проверки всех входных данных
    try:
        write_report(report_path, matrix)
        export_to_csv(csv_path, matrix)
    except OSError as err:
        print(f"Ошибка файловой системы при сохранении отчета: {err}")
        return

    print("Матрица успешно прочитана:")
    for row in matrix:
        print(*row)

    print(f"\nОтчет успешно сформирован и сохранен в: {report_path.name}")
    print(f"Таблица экспортирована в CSV файл: {csv_path.name}")

    print("\nСодержимое сформированного отчета:")
    with open(report_path, "r", encoding="utf-8") as f:
        print(f.read().rstrip("\n"))


if __name__ == "__main__":
    main()
