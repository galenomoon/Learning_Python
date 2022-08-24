numbers = list(range(0, 21))

# "filter(lambda name: ..., [Array])" === [Array].filter.((name) => ...)
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)