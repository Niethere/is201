price_per_kg = float(input("1 кг"))
for i in range(1, 11):
    weight = i / 10
    cost = price_per_kg * weight
    print(f"{weight:.1f} кг конфет стоит {cost:.2f}")