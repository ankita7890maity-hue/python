original = [1, 2, 3, 4, 5]
part1 = original[:3]
part2 = original[3:]
part1.reverse()
part2.reverse()
result = part1 + part2
print(result)