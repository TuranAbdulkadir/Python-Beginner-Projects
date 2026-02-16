# Rock Band Name Generator
import random
adj = ["Midnight","Electric","Cosmic","Shadow","Neon","Crystal","Thunder","Digital","Cyber","Phantom"]
nouns = ["Dragons","Wolves","Phoenix","Serpents","Knights","Pirates","Storm","Pulse","Venom","Echo"]
name = f"{random.choice(adj)} {random.choice(nouns)}"
print(f"\n🎸 Your band name: {name}")
print("\nMore suggestions:")
for _ in range(4):
    print(f"  - {random.choice(adj)} {random.choice(nouns)}")
