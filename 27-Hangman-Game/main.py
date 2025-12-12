import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["python", "joker", "hacker", "matrix", "galaxy"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print("☠️ ADAM ASMACA BAŞLADI ☠️")

end_of_game = False
while not end_of_game:
    guess = input("Bir harf tahmin et: ").lower()

    if guess in display:
        print(f"{guess} harfini zaten buldun.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"'{guess}' kelimede yok. Bir can gitti!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("💀 KAYBETTİN! Kelime: " + chosen_word)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("🏆 KAZANDIN!")

    print(stages[lives])