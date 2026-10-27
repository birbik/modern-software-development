# logic.py — Бизнес-логика управления списком книг

def validate_records(records):
    """Проверяет корректность структуры и типов данных списка записей.
    
    Корень должен быть списком словарей с обязательными ключами:
    - id (уникальное целое положительное число);
    - title (непустая строка);
    - category (непустая строка);
    - amount (целое неотрицательное число);
    - completed (строго логическое значение bool).
    При нарушении возбуждает ValueError.
    """
    if not isinstance(records, list):
        raise ValueError("Данные должны быть представлены списком")

    seen_ids = set()
    for idx, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"Запись с индексом {idx} должна быть словарем")

        # Проверка обязательных полей
        required_keys = ("id", "title", "category", "amount", "completed")
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Запись {idx}: отсутствует обязательное поле '{key}'")

        # Проверка id
        id_val = item["id"]
        if type(id_val) is not int or id_val <= 0:
            raise ValueError(f"Запись {idx}: поле 'id' должно быть положительным целым числом, получено {repr(id_val)}")
        if id_val in seen_ids:
            raise ValueError(f"Запись {idx}: обнаружен неуникальный id={id_val}")
        seen_ids.add(id_val)

        # Проверка title
        title_val = item["title"]
        if type(title_val) is not str or not title_val.strip():
            raise ValueError(f"Запись {idx}: поле 'title' должно быть непустой строкой")

        # Проверка category
        category_val = item["category"]
        if type(category_val) is not str or not category_val.strip():
            raise ValueError(f"Запись {idx}: поле 'category' должно быть непустой строкой")

        # Проверка amount
        amount_val = item["amount"]
        if type(amount_val) is not int or amount_val < 0:
            raise ValueError(f"Запись {idx}: поле 'amount' должно быть целым числом >= 0, получено {repr(amount_val)}")

        # Проверка completed
        completed_val = item["completed"]
        if type(completed_val) is not bool:
            raise ValueError(f"Запись {idx}: поле 'completed' должно быть логическим (true/false), получено {repr(completed_val)}")

    return True


def generate_next_id(records):
    """Возвращает следующий уникальный идентификатор для новой записи."""
    return max([r["id"] for r in records], default=0) + 1


def add_record(records, title, category, amount):
    """Добавляет новую книгу в список. Начальный статус completed — False.
    
    Модифицирует records на месте и возвращает добавленную запись.
    """
    cleaned_title = title.strip()
    cleaned_category = category.strip()

    if not cleaned_title:
        raise ValueError("Название не должно быть пустым")
    if not cleaned_category:
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество страниц должно быть целым неотрицательным числом")

    new_id = generate_next_id(records)
    new_record = {
        "id": new_id,
        "title": cleaned_title,
        "category": cleaned_category,
        "amount": amount,
        "completed": False,
    }
    records.append(new_record)
    return new_record


def find_records(records, query):
    """Выполняет поиск записей по подстроке в названии без учета регистра.
    
    Возвращает новый список найденных записей. Исходный список не изменяется.
    При пустом запросе возбуждает ValueError.
    """
    cleaned_query = query.strip()
    if not cleaned_query:
        raise ValueError("Поисковый запрос не должен быть пустым")

    lower_query = cleaned_query.lower()
    return [r for r in records if lower_query in r["title"].lower()]


def set_completed(records, record_id, completed):
    """Устанавливает статус прочтения книги по ее ID.
    
    Возвращает True в случае успеха и False, если запись не найдена.
    """
    if type(completed) is not bool:
        raise ValueError("Статус должен быть логическим значением (bool)")

    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись с указанным ID из списка.
    
    Возвращает True в случае успешного удаления и False, если запись не найдена.
    Идентификаторы других записей не перенумеровываются.
    """
    for idx, r in enumerate(records):
        if r["id"] == record_id:
            records.pop(idx)
            return True
    return False


def statistics(records):
    """Вычисляет сводную статистику по текущему набору записей.
    
    Возвращает словарь:
    - total_count: общее количество записей;
    - completed_count: количество выполненных (прочитанных);
    - incomplete_count: количество невыполненных (не прочитанных);
    - total_amount: общая сумма страниц;
    - category_amounts: словарь сумм страниц по категориям (категории очищены от краевых пробелов).
    Исходный список не изменяется.
    """
    total_count = len(records)
    completed_count = sum(1 for r in records if r["completed"])
    incomplete_count = total_count - completed_count
    total_amount = sum(r["amount"] for r in records)

    category_amounts = {}
    for r in records:
        cat = r["category"].strip()
        category_amounts[cat] = category_amounts.get(cat, 0) + r["amount"]

    return {
        "total_count": total_count,
        "completed_count": completed_count,
        "incomplete_count": incomplete_count,
        "total_amount": total_amount,
        "category_amounts": category_amounts,
    }
