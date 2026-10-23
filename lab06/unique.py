# unique.py — Удаление повторов с сохранением порядка первого появления

# Ввод чисел одной строкой
raw = input("Введите целые числа через пробел: ")
numbers = [int(p) for p in raw.split()]

# Формирование списка уникальных элементов без использования set
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Вывод результата
print(unique_numbers)
