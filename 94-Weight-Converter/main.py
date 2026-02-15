# Weight Converter
weight = float(input("Enter weight: "))
unit = input("From (kg/lb/oz/g): ").lower()
conversions = {
    "kg": {"lb": 2.205, "oz": 35.274, "g": 1000, "kg": 1},
    "lb": {"kg": 0.4536, "oz": 16, "g": 453.6, "lb": 1},
    "oz": {"kg": 0.02835, "lb": 0.0625, "g": 28.35, "oz": 1},
    "g": {"kg": 0.001, "lb": 0.002205, "oz": 0.03527, "g": 1}
}
if unit in conversions:
    print(f"\n{weight} {unit} =")
    for u, factor in conversions[unit].items():
        if u != unit:
            print(f"  {weight * factor:.4f} {u}")
