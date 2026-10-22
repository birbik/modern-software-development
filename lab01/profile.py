# profile.py — Карточка студента
# Запрашиваем семь значений у пользователя

surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет): "))
favorite_subject = input("Любимый предмет: ")
weekly_hours = float(input("Часов подготовки в неделю: "))

# Расчёты
future_age = age + 4
four_weeks_hours = weekly_hours * 4
daily_hours = weekly_hours / 7

# Вывод карточки
print()
print("===== Карточка студента =====")
print(f"Имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через четыре года: {future_age}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Часов подготовки в неделю: {weekly_hours:.2f}")
print(f"За четыре недели: {four_weeks_hours:.2f} ч")
print(f"В среднем в день: {daily_hours:.2f} ч")
print("=============================")
