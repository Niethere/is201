N = int(input("Введите целое число N (> 0): "))
s = 0.0
for i in range(1, N + 1):
    s = s + 1 / i
print("Сумма:", s)