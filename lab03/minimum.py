# minimum.py — Поиск минимума трёх чисел

# Ввод трёх целых чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Поиск минимума
minimum = a

if b < minimum:
    minimum = b

if c < minimum:
    minimum = c

# Вывод результата
print(f"Минимум: {minimum}")
