# functions.py — Модуль математических и строковых функций

def sum_digits(number):
    """Возвращает сумму цифр модуля целого числа."""
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def average(numbers):
    """Возвращает среднее арифметическое чисел или None для пустого списка."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Возвращает текст в нижнем регистре с одним пробелом между словами."""
    return " ".join(text.split()).lower()


def select_numbers(numbers, threshold):
    """Возвращает новый список чисел, строго меньших заданного порога."""
    return [x for x in numbers if x < threshold]


def is_palindrome(text):
    """Проверяет строку на палиндром без учета регистра и пробелов."""
    cleaned = text.lower().replace(" ", "")
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]
