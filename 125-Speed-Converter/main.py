# Speed Converter
speed = float(input("Enter speed: "))
unit = input("Unit (kmh/mph/ms/knots): ").lower()
convert = {
    "kmh": {"mph": 0.6214, "ms": 0.2778, "knots": 0.5400, "kmh": 1},
    "mph": {"kmh": 1.6093, "ms": 0.4470, "knots": 0.8689, "mph": 1},
    "ms": {"kmh": 3.6, "mph": 2.2369, "knots": 1.9438, "ms": 1},
    "knots": {"kmh": 1.852, "mph": 1.1508, "ms": 0.5144, "knots": 1}
}
if unit in convert:
    print(f"\n{speed} {unit} =")
    for u, f in convert[unit].items():
        if u != unit: print(f"  {speed*f:.2f} {u}")
