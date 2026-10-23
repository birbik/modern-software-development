# transform.py — Замена отрицательных чисел их модулями

# Ввод чисел одной строкой
raw = input("Введите целые числа через пробел: ")
numbers = [int(p) for p in raw.split()]

# Создание нового списка с заменой отрицательных чисел на модули
transformed = [abs(num) for num in numbers]

# Вывод исходного и нового списков
print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
