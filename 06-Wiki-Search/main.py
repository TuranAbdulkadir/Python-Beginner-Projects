import wikipedia
wikipedia.set_lang("en")
q = input("Search Topic: ")
try:
    print(wikipedia.summary(q, sentences=2))
except:
    print("Not found.")