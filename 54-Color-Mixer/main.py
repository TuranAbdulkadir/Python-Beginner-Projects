# Color Mixer - RGB
def mix(c1, c2):
    return tuple((a + b) // 2 for a, b in zip(c1, c2))

def to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

colors = {
    "red": (255,0,0), "green": (0,255,0), "blue": (0,0,255),
    "yellow": (255,255,0), "cyan": (0,255,255), "magenta": (255,0,255),
    "white": (255,255,255), "orange": (255,165,0), "purple": (128,0,128)
}
print("Colors:", ", ".join(colors.keys()))
c1 = input("First color: ").lower()
c2 = input("Second color: ").lower()
if c1 in colors and c2 in colors:
    mixed = mix(colors[c1], colors[c2])
    print(f"\n{c1} + {c2} = RGB{mixed} | HEX: {to_hex(mixed)}")
else:
    print("Invalid color!")
