# analysis.py — Валидация и анализ набора задач

def validate_todos(data):
    """Проверяет структуру списка задач.
    
    Корень должен быть списком словарей.
    Каждый элемент должен содержать:
    - положительный целочисленный id (уникальный);
    - положительный целочисленный userId;
    - непустую строку title;
    - логическое поле completed (bool).
    При нарушении возбуждает ValueError с подробным описанием ошибки.
    """
    if not isinstance(data, list):
        raise ValueError("Корневой элемент данных должен быть списком")

    seen_ids = set()
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент с индексом {idx} должен быть словарем")

        # Проверка id
        if "id" not in item:
            raise ValueError(f"Элемент {idx}: отсутствует обязательное поле 'id'")
        id_val = item["id"]
        if type(id_val) is not int or id_val <= 0:
            raise ValueError(f"Элемент {idx}: поле 'id' должно быть положительным целым числом, получено {repr(id_val)}")
        if id_val in seen_ids:
            raise ValueError(f"Элемент {idx}: обнаружен неуникальный id={id_val}")
        seen_ids.add(id_val)

        # Проверка userId
        if "userId" not in item:
            raise ValueError(f"Элемент {idx}: отсутствует обязательное поле 'userId'")
        user_id_val = item["userId"]
        if type(user_id_val) is not int or user_id_val <= 0:
            raise ValueError(f"Элемент {idx}: поле 'userId' должно быть положительным целым числом, получено {repr(user_id_val)}")

        # Проверка title
        if "title" not in item:
            raise ValueError(f"Элемент {idx}: отсутствует обязательное поле 'title'")
        title_val = item["title"]
        if type(title_val) is not str or not title_val.strip():
            raise ValueError(f"Элемент {idx}: поле 'title' должно быть непустой строкой")

        # Проверка completed
        if "completed" not in item:
            raise ValueError(f"Элемент {idx}: отсутствует обязательное поле 'completed'")
        completed_val = item["completed"]
        if type(completed_val) is not bool:
            raise ValueError(f"Элемент {idx}: поле 'completed' должно быть логическим (true/false), получено {repr(completed_val)}")

    return True


def completion_counts(todos):
    """Возвращает словарь количества выполненных задач для всех пользователей из набора.
    
    Пользователи без завершенных задач также включаются со значением 0.
    """
    counts = {task["userId"]: 0 for task in todos}
    for task in todos:
        if task["completed"]:
            counts[task["userId"]] += 1
    return counts


def top_users(counts):
    """Возвращает отсортированный список ID пользователей с максимальным числом выполненных задач.
    
    Для пустого словаря или если максимум равен 0, возвращает [].
    """
    if not counts:
        return []
    max_count = max(counts.values())
    if max_count == 0:
        return []
    return sorted([user_id for user_id, cnt in counts.items() if cnt == max_count])


def get_leader_tasks(todos, leaders):
    """Возвращает завершенные задачи пользователей-лидеров с сохранением исходного порядка."""
    leader_set = set(leaders)
    return [task for task in todos if task["userId"] in leader_set and task["completed"]]


def select_tasks(todos, user_id, parameter=None):
    """Вариант 2: возвращает список завершенных задач указанного пользователя.
    
    Параметр не требуется (None). Исходный список не модифицируется.
    """
    return [task.copy() for task in todos if task["userId"] == user_id and task["completed"]]
