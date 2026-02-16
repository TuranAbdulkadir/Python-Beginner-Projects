# Compass Direction
degrees = float(input("Enter degrees (0-360): "))
directions = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
idx = round(degrees / 22.5) % 16
print(f"\n{degrees}° = {directions[idx]}")
