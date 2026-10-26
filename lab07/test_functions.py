# test_functions.py — Автоматические проверки функций

from functions import average, is_palindrome, normalize_text, select_numbers, sum_digits

# Базовые проверки суммы цифр
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

# Базовые проверки вычисления среднего
assert average([]) is None
assert average([2, 4, 6]) == 4
avg_float = average([1, 2])
assert avg_float is not None and abs(avg_float - 1.5) < 1e-9

# Базовые проверки нормализации текста
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Проверки индивидуального варианта (Вариант 2: Меньше порога)
# 1. Контрольный пример из методички
assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0]

# 2. Пустой список
assert select_numbers([], 2) == []

# 3. Граничные значения: элементы, равные порогу, не включаются
assert select_numbers([1, 2, 3], 2) == [1]
assert select_numbers([-2, -1, 0, 1], 0) == [-2, -1]

# 4. Сохранение повторов
assert select_numbers([-5, 0, -5, 2], 2) == [-5, 0, -5]

# 5. Исходный список не изменяется
original = [-5, 0, 2, 5]
copy_orig = original.copy()
_ = select_numbers(original, 2)
assert original == copy_orig

# Проверки функции проверки на палиндром
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("Шалаш") is True
assert is_palindrome("Python") is False
assert is_palindrome("   ") is False
assert is_palindrome("") is False
assert is_palindrome("А!") is False

print("Все проверки пройдены успешно!")
