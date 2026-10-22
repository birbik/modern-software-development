# range_numbers.py — Вывод чисел диапазона в обе стороны

# Ввод границ диапазона
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Определение направления шага
if a <= b:
    step = 1
else:
    step = -1

# Вывод чисел диапазона включительно
for number in range(a, b + step, step):
    print(number)
