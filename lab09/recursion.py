# recursion.py — Рекурсивное и итеративное вычисление факториала

def factorial_recursive(number):
    """Рекурсивное вычисление факториала (для целых чисел от 0 до 20)."""
    if number == 0:
        return 1
    return number * factorial_recursive(number - 1)


def factorial_iterative(number):
    """Итеративное вычисление факториала циклом (для целых чисел от 0 до 20)."""
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def trace_factorial_3():
    """Пошаговая трассировка рекурсивного вычисления factorial(3)."""
    print("Трассировка вызова factorial(3):")
    print("  Шаг 1: вызов factorial(3) -> ожидает 3 * factorial(2)")
    print("  Шаг 2: вызов factorial(2) -> ожидает 2 * factorial(1)")
    print("  Шаг 3: вызов factorial(1) -> ожидает 1 * factorial(0)")
    print("  Шаг 4: вызов factorial(0) -> базовый случай, возврат 1")
    print("  Шаг 5: возврат из factorial(1) -> 1 * 1 = 1")
    print("  Шаг 6: возврат из factorial(2) -> 2 * 1 = 2")
    print("  Шаг 7: возврат из factorial(3) -> 3 * 2 = 6")
    print("Итоговый результат:", factorial_recursive(3))


def main():
    # Проверка совпадения результатов для чисел от 0 до 20
    for n in range(21):
        rec = factorial_recursive(n)
        it = factorial_iterative(n)
        assert rec == it, f"Несовпадение для n={n}: {rec} != {it}"

    print("Сравнение рекурсивного и итеративного факториала для 0..20: все значения совпадают!")
    print()
    trace_factorial_3()


if __name__ == "__main__":
    main()
