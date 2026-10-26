# main.py — Демонстрация работы функций

from functions import average, is_palindrome, normalize_text, select_numbers, sum_digits


def main():
    # Демонстрация sum_digits
    raw_num = input("Введите целое число: ")
    num = int(raw_num)
    print(f"Сумма цифр: {sum_digits(num)}")

    # Демонстрация average
    raw_nums = input("Введите целые числа через пробел: ")
    parts = raw_nums.split()
    numbers = [int(p) for p in parts]
    avg = average(numbers)
    if avg is None:
        print("Среднее значение: Нет данных")
    else:
        print(f"Среднее значение: {avg:.2f}")

    # Демонстрация select_numbers (Вариант 2: Меньше порога)
    threshold = int(input("Введите порог для выборки: "))
    selected = select_numbers(numbers, threshold)
    print(f"Числа меньше {threshold}: {selected}")

    # Демонстрация normalize_text и is_palindrome
    text = input("Введите текст: ")
    normalized = normalize_text(text)
    print(f"Нормализованный текст: {normalized}")
    pal = is_palindrome(text)
    print(f"Палиндром: {'Да' if pal else 'Нет'}")


if __name__ == "__main__":
    main()
