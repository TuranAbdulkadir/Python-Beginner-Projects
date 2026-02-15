# Simple Chatbot
responses = {
    "hello": "Hi there! How can I help?",
    "how are you": "I'm a bot, but I'm doing great!",
    "name": "I'm PyBot 1.0!",
    "time": "I don't have a watch, sorry!",
    "joke": "Why do programmers prefer dark mode? Light attracts bugs!",
    "bye": "Goodbye! Have a great day!"
}
print("=== PyBot ===")
print("Say hello, ask my name, or say bye")
while True:
    msg = input("\nYou: ").lower().strip()
    if msg == "bye": print("Bot:", responses["bye"]); break
    replied = False
    for key, val in responses.items():
        if key in msg: print(f"Bot: {val}"); replied = True; break
    if not replied: print("Bot: I don't understand. Try 'hello' or 'joke'")
