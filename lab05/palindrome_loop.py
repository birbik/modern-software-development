# palindrome_loop.py — Проверка на палиндром с помощью цикла

# Ввод строки
text = input("Введите текст: ")

# Очистка строки
cleaned = text.lower().replace(" ", "")

# Проверка без среза через цикл по первой половине строки
if len(cleaned) == 0:
    print("Нет текста")
else:
    is_palindrome = True
    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            is_palindrome = False
            break

    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
