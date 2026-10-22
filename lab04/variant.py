# variant.py — Вариант 2: Отрицательные числа

# Ввод количества чисел
n = int(input("Введите количество чисел (n >= 0): "))
count = 0
total = 0

# Обработка потока чисел в одном цикле
for _ in range(n):
    number = int(input("Введите число: "))
    if number < 0:
        count += 1
        total += number

# Вывод результатов
print(f"Количество: {count}")
print(f"Сумма: {total}")
