# Zodiac Sign Finder
month = int(input("Birth month (1-12): "))
day = int(input("Birth day: "))
signs = [
    (1,20,"Capricorn"),(2,19,"Aquarius"),(3,20,"Pisces"),(4,20,"Aries"),
    (5,21,"Taurus"),(6,21,"Gemini"),(7,22,"Cancer"),(8,23,"Leo"),
    (9,23,"Virgo"),(10,23,"Libra"),(11,22,"Scorpio"),(12,22,"Sagittarius")
]
sign = "Capricorn"
for i, (m, d, s) in enumerate(signs):
    if (month == m and day <= d) or (month == signs[i-1][0] if i > 0 else 12 and day > signs[i-1][1] if i > 0 else 22):
        sign = s
        break
traits = {"Aries":"Bold","Taurus":"Reliable","Gemini":"Curious","Cancer":"Caring",
          "Leo":"Confident","Virgo":"Analytical","Libra":"Diplomatic","Scorpio":"Passionate",
          "Sagittarius":"Adventurous","Capricorn":"Disciplined","Aquarius":"Independent","Pisces":"Creative"}
print(f"\nYour sign: {sign}")
print(f"Trait: {traits.get(sign, 'Unknown')}")
