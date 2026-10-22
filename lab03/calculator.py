# calculator.py — Калькулятор с выбором операции

# Ввод двух вещественных чисел и операции
first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

# Вычисление результата
if operation == "+":
    print(f"Результат: {first + second:.2f}")
elif operation == "-":
    print(f"Результат: {first - second:.2f}")
elif operation == "*":
    print(f"Результат: {first * second:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"Результат: {first / second:.2f}")
else:
    print("Неизвестная операция")
