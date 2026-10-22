# variant.py — Вариант 2: Книжный магазин (Учебники / Сборники задач)
# Расчёт заказа из двух позиций с доставкой и скидкой

# Ввод общих данных заказа
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Ввод данных первой позиции (Учебники)
first_item_name = input("Название первой позиции: ")
first_quantity = int(input(f"Количество ({first_item_name}): "))
first_price = float(input(f"Цена за единицу ({first_item_name}), руб.: "))

# Ввод данных второй позиции (Сборники задач)
second_item_name = input("Название второй позиции: ")
second_quantity = int(input(f"Количество ({second_item_name}): "))
second_price = float(input(f"Цена за единицу ({second_item_name}), руб.: "))

# Ввод стоимости доставки, скидки и внесённой суммы
delivery_cost = float(input("Стоимость доставки, руб.: "))
discount_percent = float(input("Скидка на товары (%): "))
paid_amount = float(input("Внесённая сумма, руб.: "))

# Расчёты
first_cost = first_quantity * first_price
second_cost = second_quantity * second_price
goods_cost = first_cost + second_cost
discount_amount = goods_cost * discount_percent / 100
goods_after_discount = goods_cost - discount_amount
total_cost = goods_after_discount + delivery_cost
total_quantity = first_quantity + second_quantity
change = paid_amount - total_cost

# Вывод результатов
print()
print(f"===== {order_name} =====")
print(f"Заказчик: {customer_name}")
print()
print(f"{'Название':<25} | {'Кол-во':>6} | {'Цена':>10} | {'Стоимость':>10}")
print("-" * 62)
print(f"{first_item_name:<25} | {first_quantity:>6} | {first_price:>10.2f} | {first_cost:>10.2f}")
print(f"{second_item_name:<25} | {second_quantity:>6} | {second_price:>10.2f} | {second_cost:>10.2f}")
print("-" * 62)
print(f"Общее количество единиц: {total_quantity}")
print(f"Стоимость товаров (без доставки): {goods_cost:.2f} руб.")
print(f"Скидка ({discount_percent:.0f}%): -{discount_amount:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_after_discount:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итого к оплате: {total_cost:.2f} руб.")
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
