price_per_kg = float(input("Введите цену за 1 кг конфет: "))

weight = 1.2
while weight <= 2.0:
    cost = price_per_kg * weight
    print(f"{weight:.1f} кг конфет стоит {cost:.2f}")
    weight += 0.2