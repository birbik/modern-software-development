# test_collections.py — Автоматические проверки коллекций

from collections_lab import (
    BOOK_RECORDS,
    all_topics,
    common_topics,
    demo_record,
    sorted_category_totals,
    titles_in_category,
    totals_by_category,
    word_counts,
)

# 1. Проверки подсчета частот слов
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("   ") == {}
assert word_counts("один один два. ДВА? два") == {"один": 2, "два": 3}

# 2. Проверки общих и уникальных тем
assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
assert common_topics([], ["sql", "git"]) == []
assert all_topics([], ["sql", "git"]) == ["git", "sql"]
assert common_topics([], []) == []
assert all_topics([], []) == []

# 3. Проверки записи и кортежа
record, pair = demo_record()
assert record == {"title": "Python", "hours": 6, "completed": False}
assert pair == ("Python", 6)

# 4. Проверки контрольного примера из методички
sample_records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]

assert totals_by_category(sample_records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(sample_records, "основное") == ["A", "C"]
assert titles_in_category(sample_records, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []

# Проверка неизменяемости исходного списка и записей
sample_copy = [r.copy() for r in sample_records]
_ = totals_by_category(sample_records)
_ = titles_in_category(sample_records, "основное")
assert sample_records == sample_copy

# 5. Проверки для каталога книг (Вариант 2)
assert totals_by_category(BOOK_RECORDS) == {
    "Программирование": 15,
    "Алгоритмы": 3,
    "Архитектура": 2,
}
assert titles_in_category(BOOK_RECORDS, "Программирование") == [
    "Изучаем Python",
    "Чистый код",
    "Совершенный код",
]
assert titles_in_category(BOOK_RECORDS, "Алгоритмы") == ["Грокаем алгоритмы"]
assert titles_in_category(BOOK_RECORDS, "Архитектура") == ["Паттерны проектирования"]
assert titles_in_category(BOOK_RECORDS, "Кулинария") == []

# 6. Проверки сортировки категорий по сумме и названию
assert sorted_category_totals(sample_records) == [
    ("основное", 7),
    ("дополнительное", 2),
]
assert sorted_category_totals(BOOK_RECORDS) == [
    ("Программирование", 15),
    ("Алгоритмы", 3),
    ("Архитектура", 2),
]

# Проверка одинаковых сумм (сортировка по алфавиту)
tie_records = [
    {"title": "Книга 1", "category": "Языки", "amount": 5},
    {"title": "Книга 2", "category": "Базы данных", "amount": 5},
]
assert sorted_category_totals(tie_records) == [
    ("Базы данных", 5),
    ("Языки", 5),
]

print("Все проверки пройдены успешно!")
