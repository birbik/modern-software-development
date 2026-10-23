# replace.py — Замена двоеточий на дефисы с подсчётом

# Ввод строки
text = input("Введите текст: ")

# Подсчёт количества двоеточий и замена на дефисы
count = text.count(":")
replaced_text = text.replace(":", "-")

# Вывод результатов
print(f"Количество замен: {count}")
print(f"Результат: {replaced_text}")
