# storage.py — Чтение и сохранение данных в формате JSON

import json
from pathlib import Path
from logic import validate_records


def load_records(path):
    """Загружает список записей из JSON-файла по указанному пути.
    
    Проверяет валидность структуры с помощью validate_records.
    При отсутствии файла возбуждает FileNotFoundError.
    При синтаксических ошибках JSON возбуждает json.JSONDecodeError.
    При ошибках структуры возбуждает ValueError.
    """
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    validate_records(data)
    return data


def save_records(path, records):
    """Сохраняет список записей в JSON-файл в кодировке UTF-8 с отступами.
    
    Перед сохранением выполняет проверку валидности данных.
    """
    validate_records(records)
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
