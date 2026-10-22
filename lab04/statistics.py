# statistics.py — Статистика числовой последовательности

# Ввод количества чисел
n = int(input("Введите количество чисел (n >= 1): "))

# Ввод и обработка первого числа
first = int(input("Введите число: "))
total = first
positive_count = 1 if first > 0 else 0
maximum = first

# Обработка остальных чисел
for _ in range(n - 1):
    number = int(input("Введите число: "))
    total += number

    if number > 0:
        positive_count += 1

    if number > maximum:
        maximum = number

# Вывод результатов
print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")
