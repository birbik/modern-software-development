# time_parts.py — Перевод общего количества секунд в часы, минуты и секунды

# Константы для перевода единиц времени
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600

# Ввод общего количества секунд
total_seconds = int(input("Введите общее количество секунд: "))

# Расчёты: сначала выделяем часы, затем минуты и секунды из остатка
hours = total_seconds // SECONDS_PER_HOUR
after_hours = total_seconds % SECONDS_PER_HOUR
minutes = after_hours // SECONDS_PER_MINUTE
seconds = after_hours % SECONDS_PER_MINUTE

# Вывод результата
print(f"{hours} ч {minutes} мин {seconds} с")
