# Emoji Dictionary
emojis = {
    "happy": "😊", "sad": "😢", "love": "❤️", "fire": "🔥",
    "star": "⭐", "sun": "☀️", "moon": "🌙", "rocket": "🚀",
    "python": "🐍", "coffee": "☕", "music": "🎵", "game": "🎮",
    "book": "📚", "robot": "🤖", "ghost": "👻", "rain": "🌧️"
}
print("=== Emoji Dictionary ===")
print("Words:", ", ".join(emojis.keys()))
while True:
    w = input("\nEnter a word (quit to exit): ").lower()
    if w == "quit":
        print("Bye! 👋")
        break
    print(emojis.get(w, "❓ Not found. Try another!"))
