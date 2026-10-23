# positions.py — Поиск индексов максимального элемента

# Ввод чисел одной строкой
raw = input("Введите целые числа через пробел: ")
parts = raw.split()

# Проверка на пустой ввод
if not parts:
    print("Нет данных")
else:
    numbers = [int(p) for p in parts]
    max_val = max(numbers)
    indexes = []
    for i, val in enumerate(numbers):
        if val == max_val:
            indexes.append(i)
    print(indexes)
