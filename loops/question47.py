
# [::-1] reverses the list to ['e', 'd', 'c', 'b', 'a'].
# The loop prints 'e', then 'd', then encounters 'c' and breaks.
items = ['a', 'b', 'c', 'd', 'e']
for item in items[::-1]:
    print(item)
    if item == 'c':
        break
print("items")
