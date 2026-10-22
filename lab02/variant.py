# variant.py — Вариант 2: Книги и коробки
# Общий объём: Количество книг
# Вместимость единицы: Книг в коробке

# Ввод данных
total_books = int(input("Введите количество книг: "))
box_capacity = int(input("Введите вместимость одной коробки (книг в коробке): "))

# Расчёты
full_boxes = total_books // box_capacity
remainder = total_books % box_capacity
total_boxes_needed = (total_books + box_capacity - 1) // box_capacity

# Вывод результатов
print()
print("===== Размещение книг по коробкам =====")
print(f"Полных коробок: {full_boxes}")
print(f"Остаток книг: {remainder}")
print(f"Всего требуется коробок: {total_boxes_needed}")
