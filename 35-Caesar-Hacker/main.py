message = input("Şifreli mesajı gir (Encrypted message): ").lower()
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print("\n--- KIRMA İŞLEMİ BAŞLATILDI ---\n")

# Her olası anahtarı dene (0-25 arası)
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
            
    print(f'Key #{key}: {translated}')
    
print("\n--- LİSTEDEN ANLAMLI OLANI BUL ---")   