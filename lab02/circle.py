# circle.py — Вычисление длины окружности и площади круга
import math

# Ввод радиуса круга
radius = float(input("Введите радиус круга: "))

# Расчёты с использованием константы math.pi
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Вывод результатов с округлением до двух знаков после точки
print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь: {area:.2f}")
