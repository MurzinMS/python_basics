"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите число n: "))
if n > 0:
    nn = f"{n}{n}"
    nnn = f"{nn}{n}"
    result = n + int(nn) + int(nnn)
    print(f"n + nn + nnn = {result}")
else:
>>>>>>> 36bedc5 (New_data)
    print(f"Введенное число должно быть положительным")