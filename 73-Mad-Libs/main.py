# Mad Libs Story Generator
print("=== Mad Libs ===")
adj1 = input("Adjective: ")
noun1 = input("Noun: ")
verb1 = input("Verb (past): ")
adj2 = input("Another adjective: ")
place = input("Place: ")
name = input("Name: ")

story = f"""
Once upon a time, {name} found a {adj1} {noun1} in {place}.
They {verb1} all the way home with it.
It turned out to be the most {adj2} thing ever discovered!
Everyone in {place} wanted to see the {adj1} {noun1}.
{name} became famous overnight!
"""
print(story)
