import random

chambers = [0] * 6
a = (2023 * 17) % 6  # простая псевдослучайная замена randint(0, 5)
chambers[a] = 1
b = (a * 3 + 1) % 6  # еще одна псевдослучайная замена
if chambers[b]:
    print("Бах! Вы проиграли.")
else:
    print("Щелк! Вам повезло.")