# main.py — Консольный интерфейс управления списком книг для чтения

import json
from pathlib import Path
from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
)
from storage import load_records, save_records


def print_records_table(records):
    """Выводит список книг в отформатированном виде по возрастанию ID."""
    if not records:
        print("Нет записей")
        return

    sorted_records = sorted(records, key=lambda r: r["id"])
    print("\n" + "=" * 70)
    print(f"{'ID':<4} | {'Название':<28} | {'Категория':<16} | {'Стр.':<6} | {'Статус':<12}")
    print("-" * 70)
    for r in sorted_records:
        status_str = "Прочитана" if r["completed"] else "Не прочитана"
        print(f"{r['id']:<4} | {r['title'][:28]:<28} | {r['category'][:16]:<16} | {r['amount']:<6} | {status_str:<12}")
    print("=" * 70 + "\n")


def prompt_non_empty_string(prompt):
    """Запрашивает непустую строку, очищая краевые пробелы."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: значение не должно быть пустым. Повторите ввод.")


def prompt_non_negative_int(prompt):
    """Запрашивает целое неотрицательное число."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if val < 0:
            print("Ошибка: число не должно быть отрицательным.")
            continue
        return val


def main():
    folder = Path(__file__).resolve().parent
    data_path = folder / "data.json"

    # Загрузка и предварительная проверка данных
    try:
        records = load_records(data_path)
        print(f"Данные успешно загружены из {data_path.name}. Записей: {len(records)}")
    except FileNotFoundError:
        records = []
        print("Файл данных не найден. Начат новый список.")
    except UnicodeDecodeError:
        print("Критическая ошибка: неверная кодировка файла data.json (требуется UTF-8). Запуск прекращен.")
        return
    except json.JSONDecodeError as err:
        print(f"Критическая ошибка синтаксиса JSON в {data_path.name}: {err}")
        print("Запуск прекращен без перезаписи файла.")
        return
    except ValueError as err:
        print(f"Критическая ошибка структуры данных в {data_path.name}: {err}")
        print("Запуск прекращен без перезаписи файла.")
        return
    except OSError as err:
        print(f"Критическая ошибка файловой системы при чтении: {err}")
        return

    # Главный цикл меню
    while True:
        print("\n--- Список книг для чтения (Вариант 2) ---")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Найти записи")
        print("4. Изменить статус")
        print("5. Удалить запись")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("8. Выйти")

        choice = input("Выберите пункт меню (1-8): ").strip()

        if choice == "1":
            print_records_table(records)

        elif choice == "2":
            print("\nДобавление новой книги:")
            title = prompt_non_empty_string("Введите название книги: ")
            category = prompt_non_empty_string("Введите жанр / категорию: ")
            amount = prompt_non_negative_int("Введите количество страниц: ")
            new_r = add_record(records, title, category, amount)
            print(f"Книга успешно добавлена с ID={new_r['id']}.")

        elif choice == "3":
            query = input("Введите подстроку для поиска в названии: ").strip()
            if not query:
                print("Ошибка: поисковый запрос не должен быть пустым.")
                continue
            found = find_records(records, query)
            if not found:
                print(f"По запросу '{query}' записи не найдены.")
            else:
                print(f"\nНайдено записей: {len(found)}")
                print_records_table(found)

        elif choice == "4":
            record_id = prompt_non_negative_int("Введите ID книги для изменения статуса: ")
            target = next((r for r in records if r["id"] == record_id), None)
            if not target:
                print(f"Ошибка: книга с ID={record_id} не найдена.")
                continue

            current_status = "Прочитана" if target["completed"] else "Не прочитана"
            print(f"Текущий статус книги '{target['title']}': {current_status}")
            print("1 — Установить статус 'Прочитана'")
            print("2 — Установить статус 'Не прочитана'")
            print("0 — Отмена")
            status_choice = input("Ваш выбор: ").strip()

            if status_choice == "1":
                set_completed(records, record_id, True)
                print(f"Статус книги с ID={record_id} изменен на 'Прочитана'.")
            elif status_choice == "2":
                set_completed(records, record_id, False)
                print(f"Статус книги с ID={record_id} изменен на 'Не прочитана'.")
            else:
                print("Изменение статуса отменено.")

        elif choice == "5":
            record_id = prompt_non_negative_int("Введите ID книги для удаления: ")
            target = next((r for r in records if r["id"] == record_id), None)
            if not target:
                print(f"Ошибка: книга с ID={record_id} не найдена.")
                continue

            confirm = input(f"Вы действительно хотите удалить '{target['title']}'? Введите 'да' для подтверждения: ").strip().lower()
            if confirm == "да":
                delete_record(records, record_id)
                print(f"Книга с ID={record_id} успешно удалена.")
            else:
                print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print("\n" + "=" * 40)
            print("СВОДНАЯ СТАТИСТИКА")
            print("=" * 40)
            print(f"Всего книг: {stats['total_count']}")
            print(f"Прочитано: {stats['completed_count']}")
            print(f"Не прочитано: {stats['incomplete_count']}")
            print(f"Всего страниц: {stats['total_amount']}")
            print("\nСтраниц по категориям (по алфавиту):")
            if not stats["category_amounts"]:
                print("  Нет данных по категориям")
            else:
                for cat in sorted(stats["category_amounts"]):
                    print(f"  {cat}: {stats['category_amounts'][cat]} стр.")
            print("=" * 40)

        elif choice == "7":
            try:
                save_records(data_path, records)
                print(f"Данные успешно сохранены в {data_path.name}.")
            except OSError as err:
                print(f"Ошибка сохранения данных: {err}")

        elif choice == "8":
            while True:
                save_confirm = input("Сохранить текущие данные перед выходом? (да/нет): ").strip().lower()
                if save_confirm == "да":
                    try:
                        save_records(data_path, records)
                        print(f"Данные успешно сохранены в {data_path.name}.")
                        print("Выход из программы.")
                        return
                    except OSError as err:
                        print(f"Ошибка сохранения: {err}. Возврат в меню.")
                        break
                elif save_confirm == "нет":
                    print("Выход без сохранения.")
                    return
                else:
                    print("Пожалуйста, введите 'да' или 'нет'.")

        else:
            print("Неизвестная команда. Пожалуйста, введите число от 1 до 8.")


if __name__ == "__main__":
    main()
