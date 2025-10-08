A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A >= B:
    print("A должно быть меньше B")
else:
    total = 0
    for i in range(A, B + 1):
        total += i ** 2
    print("Сумма квадратов:", total)