text = "abcdefgh"

for i, char in enumerate(text):
    if char == "f":
        break

print(f"{i},{char}")
