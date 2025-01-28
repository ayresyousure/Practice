values = input().split(' ')

X, Y, Z = map(int, values)

sorted_values = sorted([X, Y, Z])

for value in sorted_values:
    print(value)
print("\n")

for value in [X, Y, Z]:
    print(value)