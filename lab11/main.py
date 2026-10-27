# main.py — Основная программа анализа задач JSON

import json
from pathlib import Path
from analysis import (
    completion_counts,
    get_leader_tasks,
    select_tasks,
    top_users,
    validate_todos,
)


def read_positive_user_id(prompt="Введите ID пользователя (целое положительное число): "):
    """Запрашивает у пользователя положительный целый ID с повтором при ошибке."""
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
    folder = Path(__file__).resolve().parent
    todos_path = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    # 1. Чтение и валидация файла todos.json
    try:
        with open(todos_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        validate_todos(data)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден ({todos_path})")
        return
    except UnicodeDecodeError:
        print(f"Ошибка: неверная кодировка файла ({todos_path}), требуется UTF-8")
        return
    except json.JSONDecodeError as err:
        print(f"Ошибка синтаксиса JSON: {err}")
        return
    except ValueError as err:
        print(f"Ошибка структуры данных: {err}")
        return
    except OSError as err:
        print(f"Ошибка файловой системы при чтении: {err}")
        return

    # 2. Анализ выполненных задач и выявление лидеров
    counts = completion_counts(data)
    leaders = top_users(counts)
    leader_tasks = get_leader_tasks(data, leaders)

    # 3. Сохранение leaders.json
    try:
        with open(leaders_path, "w", encoding="utf-8") as file:
            json.dump(leader_tasks, file, ensure_ascii=False, indent=2)
    except OSError as err:
        print(f"Ошибка записи leaders.json: {err}")
        return

    print("Анализ задач успешно выполнен:")
    print(f"Статистика завершенных задач: {counts}")
    print(f"Лидеры по числу выполненных задач: {leaders}")
    print(f"Задачи лидеров сохранены в: {leaders_path.name} (всего задач: {len(leader_tasks)})\n")

    # 4. Индивидуальный вариант 2: завершенные задачи пользователя
    user_id = read_positive_user_id("Введите ID пользователя для выборки его завершенных задач: ")
    selected = select_tasks(data, user_id)

    # 5. Сохранение selected.json
    try:
        with open(selected_path, "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
    except OSError as err:
        print(f"Ошибка записи selected.json: {err}")
        return

    print(f"Завершенные задачи пользователя {user_id} сохранены в: {selected_path.name}")
    print(f"Найдено завершенных задач: {len(selected)}")
    for t in selected:
        print(f"  [id: {t['id']}] {t['title']}")


if __name__ == "__main__":
    main()
