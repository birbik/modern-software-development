# fetch_profile.py — Получение профиля пользователя GitHub или локального образца

import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile(login):
    """Выполняет HTTP GET запрос к GitHub API для получения профиля по логину."""
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "python-course-lab11",
        },
    )
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def load_local_profile(path):
    """Загружает локальный образец профиля из JSON файла."""
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Файл не содержит корректную структуру профиля")
    return data


def display_profile(data):
    """Общая функция вывода информации о профиле пользователя."""
    print("Данные профиля:")
    print(f"  Логин: {data.get('login')}")
    print(f"  ID: {data.get('id')}")
    print(f"  Имя: {data.get('name')}")
    print(f"  Компания: {data.get('company')}")
    print(f"  Публичных репозиториев: {data.get('public_repos')}")


def main():
    folder = Path(__file__).resolve().parent
    output = folder / "profile.json"
    sample_path = folder / "profile_sample.json"

    print("Выберите источник данных профиля:")
    print("1 — Запрос через интернет (GitHub API)")
    print("2 — Локальный учебный образец (profile_sample.json)")
    choice = input("Ваш выбор (1 или 2, по умолчанию 1): ").strip()

    data = None
    if choice == "2":
        try:
            data = load_local_profile(sample_path)
            print("\nУспешно загружен локальный учебный профиль.")
        except (FileNotFoundError, json.JSONDecodeError, ValueError, OSError) as error:
            print(f"Ошибка чтения локального файла: {error}")
            return
    else:
        login = input("Введите логин GitHub (например, octocat): ").strip()
        if not login:
            login = "octocat"
        try:
            data = fetch_profile(login)
            print(f"\nПрофиль успешно получен по сети для логина: {data['login']}")
        except HTTPError as error:
            print(f"Сервер вернул HTTP {error.code}")
            return
        except (URLError, TimeoutError, socket.timeout):
            print("Не удалось получить ответ по сети. Переключаемся на локальный образец...")
            try:
                data = load_local_profile(sample_path)
                print("Загружен локальный образец.")
            except Exception as e:
                print(f"Не удалось загрузить локальный образец: {e}")
                return
        except (ValueError, UnicodeError) as error:
            print(f"Ошибка данных: {error}")
            return
        except OSError as error:
            print(f"Ошибка доступа: {error}")
            return

    if data is not None:
        display_profile(data)
        try:
            with open(output, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"\nПрофиль сохранён в файл: {output.name}")
        except OSError as error:
            print(f"Ошибка сохранения файла: {error}")


if __name__ == "__main__":
    main()
