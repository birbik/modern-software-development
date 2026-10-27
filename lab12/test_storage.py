# test_storage.py — Автоматические проверки сохранения и загрузки данных

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records

SAMPLE_DATA = [
    {"id": 1, "title": "Изучаем Python", "category": "Программирование", "amount": 800, "completed": True},
    {"id": 2, "title": "Грокаем алгоритмы", "category": "Алгоритмы", "amount": 290, "completed": False},
]


def test_save_and_load():
    with TemporaryDirectory() as directory:
        file_path = Path(directory) / "test_data.json"
        save_records(file_path, SAMPLE_DATA)

        loaded = load_records(file_path)
        assert loaded == SAMPLE_DATA


def test_file_not_found():
    with TemporaryDirectory() as directory:
        missing_path = Path(directory) / "missing.json"
        try:
            load_records(missing_path)
            assert False, "Ожидался FileNotFoundError"
        except FileNotFoundError:
            pass


def test_corrupted_json():
    with TemporaryDirectory() as directory:
        corrupted_path = Path(directory) / "corrupted.json"
        corrupted_content = "[{bad json"
        corrupted_path.write_text(corrupted_content, encoding="utf-8")

        try:
            load_records(corrupted_path)
            assert False, "Ожидался JSONDecodeError"
        except json.JSONDecodeError:
            pass

        # Проверка, что поврежденный файл не изменился
        assert corrupted_path.read_text(encoding="utf-8") == corrupted_content


def test_invalid_structure():
    with TemporaryDirectory() as directory:
        invalid_path = Path(directory) / "invalid.json"
        invalid_content = json.dumps([{"id": 1, "title": "Без других полей"}])
        invalid_path.write_text(invalid_content, encoding="utf-8")

        try:
            load_records(invalid_path)
            assert False, "Ожидался ValueError: неполные поля"
        except ValueError:
            pass


def test_save_validation():
    with TemporaryDirectory() as directory:
        file_path = Path(directory) / "bad_save.json"
        bad_data = [{"id": 1, "title": "Книга", "category": "Жанр", "amount": -10, "completed": False}]
        try:
            save_records(file_path, bad_data)
            assert False, "Ожидался ValueError при сохранении невалидных данных"
        except ValueError:
            pass


if __name__ == "__main__":
    test_save_and_load()
    test_file_not_found()
    test_corrupted_json()
    test_invalid_structure()
    test_save_validation()
    print("Все тесты модуля хранения пройдены успешно!")
