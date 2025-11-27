from gtts import gTTS
import os
text = input("Enter text: ")
tts = gTTS(text=text, lang='en')
tts.save("audio.mp3")
os.system("start audio.mp3")