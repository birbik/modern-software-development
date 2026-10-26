# collections_lab.py — Словари, множества и кортежи

# Записи для варианта 2 (Каталог книг, amount — количество экземпляров)
BOOK_RECORDS = [
    {"title": "Изучаем Python", "category": "Программирование", "amount": 5},
    {"title": "Грокаем алгоритмы", "category": "Алгоритмы", "amount": 3},
    {"title": "Чистый код", "category": "Программирование", "amount": 4},
    {"title": "Паттерны проектирования", "category": "Архитектура", "amount": 2},
    {"title": "Совершенный код", "category": "Программирование", "amount": 6},
]


def word_counts(text):
    """Возвращает словарь частот слов в тексте (без краевых знаков препинания и в нижнем регистре)."""
    counts = {}
    for raw_word in text.lower().split():
        cleaned = raw_word.strip(".,!?;:")
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    """Выводит пары 'слово: количество' в алфавитном порядке."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Возвращает отсортированный список общих тем (пересечение множеств)."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Возвращает отсортированный список всех уникальных тем (объединение множеств)."""
    return sorted(set(first) | set(second))


def demo_record():
    """Демонстрация изменения словаря и распаковки кортежа."""
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    pair = (record["title"], record["hours"])
    name, count = pair
    print(f"Запись: {record}")
    print(f"Пара из кортежа: {name}, {count}")
    return record, pair


def totals_by_category(records):
    """Возвращает словарь сумм amount по категориям."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Возвращает список названий для указанной категории в исходном порядке."""
    return [record["title"] for record in records if record["category"] == category]


def sorted_category_totals(records):
    """Возвращает список пар (category, total), отсортированных по убыванию суммы, затем по названию."""
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))


def main():
    # Частоты слов
    text = input("Введите текст для подсчета частот слов: ")
    counts = word_counts(text)
    print("Частоты слов (по алфавиту):")
    print_word_counts(counts)

    # Учебные интересы
    first_input = input("Первый список тем через пробел: ")
    second_input = input("Второй список тем через пробел: ")
    first = first_input.split()
    second = second_input.split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    # Запись и пара
    print("Демонстрация словаря и кортежа:")
    demo_record()

    # Каталог книг (Вариант 2)
    print("\nСводка по категориям книг (по алфавиту):")
    totals = totals_by_category(BOOK_RECORDS)
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    search_category = input("Введите категорию для поиска книг: ")
    titles = titles_in_category(BOOK_RECORDS, search_category)
    print(f"Книги в категории '{search_category}': {titles}")

    # Сортировка по убыванию суммы и алфавиту
    print("Рейтинг категорий по количеству экземпляров:")
    for category, total in sorted_category_totals(BOOK_RECORDS):
        print(f"  {category}: {total}")


if __name__ == "__main__":
    main()
