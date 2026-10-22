# purchase.py — Расчёт стоимости покупки тетрадей и сдачи

# Ввод данных
price = int(input("Цена тетради в целых рублях: "))
count = int(input("Количество: "))
paid = int(input("Переданная сумма в рублях: "))

# Расчёты
cost = price * count
change = paid - cost

# Вывод результатов
print(f"Стоимость: {cost}")
print(f"Сдача: {change}")
