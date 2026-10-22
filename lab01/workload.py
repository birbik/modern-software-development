# workload.py — Учебная нагрузка
# Константа для перевода минут в часы
MINUTES_PER_HOUR = 60

# Ввод данных первого предмета
first_subject = input("Название первого предмета: ")
first_count = int(input(f"Количество занятий по предмету \"{first_subject}\" за неделю: "))
first_duration = int(input(f"Продолжительность одного занятия по предмету \"{first_subject}\" (мин): "))

# Ввод данных второго предмета
second_subject = input("Название второго предмета: ")
second_count = int(input(f"Количество занятий по предмету \"{second_subject}\" за неделю: "))
second_duration = int(input(f"Продолжительность одного занятия по предмету \"{second_subject}\" (мин): "))

# Ввод доступного времени
available_hours = float(input("Доступное время на неделю (часов): "))

# Расчёты
first_minutes = first_count * first_duration
second_minutes = second_count * second_duration
total_minutes = first_minutes + second_minutes
total_hours = total_minutes / MINUTES_PER_HOUR
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

# Вывод результатов
print()
print("===== Учебная нагрузка =====")
print(f"{first_subject}: {first_minutes} мин")
print(f"{second_subject}: {second_minutes} мин")
print(f"Общая нагрузка: {total_minutes} мин, или {total_hours:.2f} ч")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч")
print("============================")
