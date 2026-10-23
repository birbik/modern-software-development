# normalize.py — Нормализация текста

# Ввод исходной строки
text = input("Введите текст: ")

# Расчёт исходной длины и разбиение на слова
original_length = len(text)
words = text.split()
normalized_text = " ".join(words)
new_length = len(normalized_text)
word_count = len(words)

# Вывод результатов
print(f"Исходная длина: {original_length}")
print(f"Новая длина: {new_length}")
print(f"Количество слов: {word_count}")
print(f"Нормализованный текст: {normalized_text}")
