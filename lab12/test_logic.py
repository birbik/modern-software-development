# test_logic.py — Автоматические проверки бизнес-логики проекта

from logic import (
    add_record,
    delete_record,
    find_records,
    generate_next_id,
    set_completed,
    statistics,
    validate_records,
)


def test_validation():
    # 1. Корректные данные
    valid_data = [
        {"id": 1, "title": "Чистый код", "category": "Программирование", "amount": 460, "completed": False},
        {"id": 2, "title": "Дюна", "category": "Фантастика", "amount": 700, "completed": True},
    ]
    assert validate_records(valid_data) is True
    assert validate_records([]) is True

    # 2. Не список в корне
    try:
        validate_records({"id": 1})
        assert False, "Ожидался ValueError: корень не список"
    except ValueError:
        pass

    # 3. Элемент не словарь
    try:
        validate_records(["не словарь"])
        assert False, "Ожидался ValueError: элемент списка не словарь"
    except ValueError:
        pass

    # 4. Отсутствие обязательного поля
    missing_key = [{"id": 1, "title": "Книга", "category": "Жанр", "amount": 100}]
    try:
        validate_records(missing_key)
        assert False, "Ожидался ValueError: отсутствует completed"
    except ValueError:
        pass

    # 5. Неуникальный ID
    dup_id = [
        {"id": 1, "title": "Книга 1", "category": "Жанр", "amount": 100, "completed": False},
        {"id": 1, "title": "Книга 2", "category": "Жанр", "amount": 200, "completed": True},
    ]
    try:
        validate_records(dup_id)
        assert False, "Ожидался ValueError: дубликат ID"
    except ValueError:
        pass

    # 6. ID не целое число (логическое значение True)
    bool_id = [{"id": True, "title": "Книга", "category": "Жанр", "amount": 100, "completed": False}]
    try:
        validate_records(bool_id)
        assert False, "Ожидался ValueError: id=True"
    except ValueError:
        pass

    # 7. ID <= 0
    zero_id = [{"id": 0, "title": "Книга", "category": "Жанр", "amount": 100, "completed": False}]
    try:
        validate_records(zero_id)
        assert False, "Ожидался ValueError: id=0"
    except ValueError:
        pass

    # 8. Пустой заголовок
    empty_title = [{"id": 1, "title": "   ", "category": "Жанр", "amount": 100, "completed": False}]
    try:
        validate_records(empty_title)
        assert False, "Ожидался ValueError: пустой title"
    except ValueError:
        pass

    # 9. Отрицательный amount
    neg_amount = [{"id": 1, "title": "Книга", "category": "Жанр", "amount": -5, "completed": False}]
    try:
        validate_records(neg_amount)
        assert False, "Ожидался ValueError: amount < 0"
    except ValueError:
        pass

    # 10. Поле amount логического типа (True)
    bool_amount = [{"id": 1, "title": "Книга", "category": "Жанр", "amount": True, "completed": False}]
    try:
        validate_records(bool_amount)
        assert False, "Ожидался ValueError: amount=True"
    except ValueError:
        pass

    # 11. completed строкового типа
    str_completed = [{"id": 1, "title": "Книга", "category": "Жанр", "amount": 100, "completed": "true"}]
    try:
        validate_records(str_completed)
        assert False, "Ожидался ValueError: completed='true'"
    except ValueError:
        pass


def test_add_and_id_generation():
    records = []
    assert generate_next_id(records) == 1

    r1 = add_record(records, "  Изучаем Python  ", "  Программирование  ", 800)
    assert r1["id"] == 1
    assert r1["title"] == "Изучаем Python"
    assert r1["category"] == "Программирование"
    assert r1["amount"] == 800
    assert r1["completed"] is False
    assert len(records) == 1

    # Добавление второй книги с тем же названием
    r2 = add_record(records, "Изучаем Python", "Учебники", 500)
    assert r2["id"] == 2
    assert r2["title"] == "Изучаем Python"
    assert len(records) == 2


def test_find_records():
    records = [
        {"id": 1, "title": "Изучаем Python", "category": "IT", "amount": 800, "completed": True},
        {"id": 2, "title": "Грокаем алгоритмы", "category": "IT", "amount": 290, "completed": True},
        {"id": 3, "title": "Python для начинающих", "category": "IT", "amount": 350, "completed": False},
    ]

    # Поиск без учета регистра
    found_py = find_records(records, "PY")
    assert [r["id"] for r in found_py] == [1, 3]

    found_alg = find_records(records, "алгоритм")
    assert [r["id"] for r in found_alg] == [2]

    # Ничего не найдено
    assert find_records(records, "Кулинария") == []

    # Пустой запрос
    try:
        find_records(records, "   ")
        assert False, "Ожидался ValueError: пустой поисковый запрос"
    except ValueError:
        pass


def test_set_completed():
    records = [
        {"id": 1, "title": "Книга 1", "category": "IT", "amount": 100, "completed": False},
    ]

    # Успешное изменение
    assert set_completed(records, 1, True) is True
    assert records[0]["completed"] is True

    assert set_completed(records, 1, False) is True
    assert records[0]["completed"] is False

    # Неизвестный ID
    assert set_completed(records, 999, True) is False
    assert records[0]["completed"] is False


def test_delete_and_id_preservation():
    records = [
        {"id": 1, "title": "Книга 1", "category": "IT", "amount": 100, "completed": False},
        {"id": 2, "title": "Книга 2", "category": "IT", "amount": 200, "completed": True},
    ]

    # Удаление записи с ID 1
    assert delete_record(records, 1) is True
    assert len(records) == 1
    # Оставшаяся запись сохраняет свой ID 2
    assert records[0]["id"] == 2

    # Следующая добавленная запись получает ID 3
    r3 = add_record(records, "Книга 3", "IT", 300)
    assert r3["id"] == 3

    # Удаление неизвестного ID
    assert delete_record(records, 999) is False
    assert len(records) == 2


def test_statistics():
    # Пустой список
    s_empty = statistics([])
    assert s_empty["total_count"] == 0
    assert s_empty["completed_count"] == 0
    assert s_empty["incomplete_count"] == 0
    assert s_empty["total_amount"] == 0
    assert s_empty["category_amounts"] == {}

    # Заполненный список
    records = [
        {"id": 1, "title": "А", "category": "Программирование", "amount": 400, "completed": True},
        {"id": 2, "title": "Б", "category": "Фантастика", "amount": 200, "completed": False},
        {"id": 3, "title": "В", "category": "Программирование", "amount": 100, "completed": False},
    ]
    s = statistics(records)
    assert s["total_count"] == 3
    assert s["completed_count"] == 1
    assert s["incomplete_count"] == 2
    assert s["total_amount"] == 700
    assert s["category_amounts"] == {
        "Программирование": 500,
        "Фантастика": 200,
    }


if __name__ == "__main__":
    test_validation()
    test_add_and_id_generation()
    test_find_records()
    test_set_completed()
    test_delete_and_id_preservation()
    test_statistics()
    print("Все тесты бизнес-логики пройдены успешно!")
