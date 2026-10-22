# prime.py — Проверка простоты числа

# Ввод числа
n = int(input("Введите число (n >= 2): "))
divisor = 2
is_prime = True

# Поиск делителей до квадратного корня из n
while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1

# Вывод результата
if is_prime:
    print("Простое")
else:
    print("Составное")
