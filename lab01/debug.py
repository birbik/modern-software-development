# debug.py — Поиск и исправление ошибок

# ===== Фрагмент А =====
# Ошибка: переменные first и second содержат строки "2" и "3".
# Оператор + для строк выполняет конкатенацию, поэтому результат "23", а не 5.
# Исправление: преобразовать строки в целые числа через int().

print("--- Фрагмент А ---")

first_a = "2"
second_a = "3"

print(f"До преобразования: type(first) = {type(first_a)}, type(second) = {type(second_a)}")

first_a = int(first_a)
second_a = int(second_a)

print(f"После преобразования: type(first) = {type(first_a)}, type(second) = {type(second_a)}")
print(f"Сумма: {first_a + second_a}")
print()

# ===== Фрагмент Б =====
# Ошибка: input() возвращает строку. Попытка сложить строку "17" и число 1
# вызывает TypeError, потому что Python не может сложить str и int.
# Исправление: обернуть input() в int() для получения целого числа.

print("--- Фрагмент Б ---")

age_text = input("Возраст: ")
print(f"До преобразования: type(age) = {type(age_text)}, значение = {age_text}")

age = int(age_text)
print(f"После преобразования: type(age) = {type(age)}, значение = {age}")
print(f"Возраст через год: {age + 1}")
print()

# ===== Фрагмент В =====
# Ошибка: в выражении first + second + third / 3 деление выполняется
# раньше сложения (приоритет операций). Делится только third на 3,
# получается 4 + 7 + 3.333... = 14.333..., а не 7.0.
# Исправление: заключить сумму в скобки (first + second + third) / 3.

print("--- Фрагмент В ---")

first_c = 4
second_c = 7
third_c = 10

average = (first_c + second_c + third_c) / 3
print(f"Среднее трёх чисел ({first_c}, {second_c}, {third_c}): {average}")
