# variant.py — Вариант 2: Слова, заканчивающиеся на букву «я»

# Ввод строки
text = input("Введите текст: ")

# Обработка слов
words = text.split()
matched = []

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned:
        continue
    if cleaned.endswith("я"):
        matched.append(cleaned)

# Вывод результатов
if len(matched) == 0:
    print("Нет совпадений")
    print("Количество: 0")
else:
    for word in matched:
        print(word)
    print(f"Количество: {len(matched)}")
