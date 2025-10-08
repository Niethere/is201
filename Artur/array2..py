# Задача: создать массив из N элементов, где каждый элемент — это степень двойки от 2^1 до 2^N.

N = int(input("Введите целое число N (> 0): "))

powers_of_two = []
for i in range(1, N + 1):
    powers_of_two.append(2 ** i)

print("Массив степеней двойки:", powers_of_two)