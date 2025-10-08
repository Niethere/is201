A = int(input("Введите A: "))
B = int(input("Введите B: "))

product = 1
for i in range(A, B + 1):
    product = product * i

print("Произведение всех целых чисел от A до B:", product)