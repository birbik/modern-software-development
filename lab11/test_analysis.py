# test_analysis.py — Автоматические проверки анализа задач JSON

import json
from tempfile import TemporaryDirectory
from pathlib import Path
from analysis import (
    completion_counts,
    get_leader_tasks,
    select_tasks,
    top_users,
    validate_todos,
)

SAMPLE_TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


def test_sample_analysis():
    # Проверка учебного набора данных
    assert validate_todos(SAMPLE_TODOS) is True

    counts = completion_counts(SAMPLE_TODOS)
    assert counts == {5: 2, 10: 2}

    leaders = top_users(counts)
    assert leaders == [5, 10]

    leader_tasks = get_leader_tasks(SAMPLE_TODOS, leaders)
    assert [t["id"] for t in leader_tasks] == [1, 3, 4, 5]


def test_empty_and_zero_completed():
    # Пустой список
    assert completion_counts([]) == {}
    assert top_users({}) == []
    assert get_leader_tasks([], []) == []

    # Набор только с незавершенными задачами
    all_incomplete = [
        {"id": 1, "userId": 1, "title": "А", "completed": False},
        {"id": 2, "userId": 2, "title": "Б", "completed": False},
    ]
    counts_incomplete = completion_counts(all_incomplete)
    assert counts_incomplete == {1: 0, 2: 0}
    assert top_users(counts_incomplete) == []
    assert get_leader_tasks(all_incomplete, []) == []


def test_single_and_multiple_leaders():
    # Единственный лидер
    data_single = [
        {"id": 1, "userId": 1, "title": "А", "completed": True},
        {"id": 2, "userId": 1, "title": "Б", "completed": True},
        {"id": 3, "userId": 2, "title": "В", "completed": True},
    ]
    counts_single = completion_counts(data_single)
    assert counts_single == {1: 2, 2: 1}
    assert top_users(counts_single) == [1]

    # Несколько лидеров (из контрольного примера)
    counts_multiple = {5: 2, 10: 2, 15: 1}
    assert top_users(counts_multiple) == [5, 10]


def test_variant_2_select_tasks():
    # Вариант 2: завершенные задачи указанного пользователя
    res_5 = select_tasks(SAMPLE_TODOS, 5)
    assert [t["id"] for t in res_5] == [1, 5]

    res_10 = select_tasks(SAMPLE_TODOS, 10)
    assert [t["id"] for t in res_10] == [3, 4]

    # Неизвестный пользователь
    assert select_tasks(SAMPLE_TODOS, 999) == []

    # Пользователь без выполненных задач
    data_no_comp = [
        {"id": 1, "userId": 1, "title": "X", "completed": False},
    ]
    assert select_tasks(data_no_comp, 1) == []

    # Неизменяемость исходного списка
    todos_copy = [t.copy() for t in SAMPLE_TODOS]
    _ = select_tasks(SAMPLE_TODOS, 5)
    assert SAMPLE_TODOS == todos_copy


def test_validation_errors():
    # 1. Корневой элемент — не список (словарь)
    try:
        validate_todos({"id": 1})
        assert False, "Не обнаружена ошибка: объект вместо списка"
    except ValueError:
        pass

    # 2. Повторяющийся id
    duplicate_id = [
        {"id": 1, "userId": 1, "title": "А", "completed": True},
        {"id": 1, "userId": 2, "title": "Б", "completed": True},
    ]
    try:
        validate_todos(duplicate_id)
        assert False, "Не обнаружена ошибка: повторяющийся id"
    except ValueError:
        pass

    # 3. Отсутствующий userId
    missing_user = [
        {"id": 1, "title": "А", "completed": True},
    ]
    try:
        validate_todos(missing_user)
        assert False, "Не обнаружена ошибка: отсутствует userId"
    except ValueError:
        pass

    # 4. completed строкой вместо bool
    str_completed = [
        {"id": 1, "userId": 1, "title": "А", "completed": "false"},
    ]
    try:
        validate_todos(str_completed)
        assert False, "Не обнаружена ошибка: completed='false'"
    except ValueError:
        pass

    # 5. id=True (логическое значение вместо целого)
    bool_id = [
        {"id": True, "userId": 1, "title": "А", "completed": True},
    ]
    try:
        validate_todos(bool_id)
        assert False, "Не обнаружена ошибка: id=True"
    except ValueError:
        pass

    # 6. Пустой заголовок
    empty_title = [
        {"id": 1, "userId": 1, "title": "   ", "completed": True},
    ]
    try:
        validate_todos(empty_title)
        assert False, "Не обнаружена ошибка: пустой title"
    except ValueError:
        pass


def test_json_dump_load_equivalence():
    with TemporaryDirectory() as directory:
        test_file = Path(directory) / "test.json"
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(SAMPLE_TODOS, f, ensure_ascii=False, indent=2)

        with open(test_file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)

        assert loaded_data == SAMPLE_TODOS


if __name__ == "__main__":
    test_sample_analysis()
    test_empty_and_zero_completed()
    test_single_and_multiple_leaders()
    test_variant_2_select_tasks()
    test_validation_errors()
    test_json_dump_load_equivalence()
    print("Все проверки пройдены успешно!")
