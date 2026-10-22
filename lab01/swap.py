# swap.py — Обмен значениями двух аудиторий

# Ввод названий аудиторий
first_room = input("Название первой аудитории: ")
second_room = input("Название второй аудитории: ")

# Вывод исходных значений
print()
print("До обмена:")
print(f"  Первая аудитория: {first_room}")
print(f"  Вторая аудитория: {second_room}")

# Обмен через третью (временную) переменную
temporary = first_room
first_room = second_room
second_room = temporary

# Вывод результата после обмена
print()
print("После обмена:")
print(f"  Первая аудитория: {first_room}")
print(f"  Вторая аудитория: {second_room}")
