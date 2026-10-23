# palindrome.py — Проверка строки на палиндром

# Ввод строки
text = input("Введите текст: ")

# Очистка: нижний регистр и удаление обычных пробелов
cleaned = text.lower().replace(" ", "")

# Проверка на палиндром с помощью среза
if len(cleaned) == 0:
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
