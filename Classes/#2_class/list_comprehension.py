#listcomp

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"\nBefore Listcomp {values}")

values = [value * 2 for value in values]

print(f"\nAfter Listcomp {values}")