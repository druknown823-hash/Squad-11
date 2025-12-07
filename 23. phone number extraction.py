import re

text = input("Enter text: ")

pattern = r'\b(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4})\b'

phones = re.findall(pattern, text)

print("Extracted Phone Numbers:")
for p in phones:
    print(p)
