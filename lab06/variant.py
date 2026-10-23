# variant.py — Вариант 2: Отрицательные числа

# Ввод чисел одной строкой
raw = input("Введите целые числа через пробел: ")
numbers = [int(p) for p in raw.split()]

# Выборка отрицательных чисел
filtered = [x for x in numbers if x < 0]
count = len(filtered)
total = sum(filtered)
sorted_copy = sorted(filtered)

# Вывод результатов
print(f"Выборка: {filtered}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Сортированная копия: {sorted_copy}")
