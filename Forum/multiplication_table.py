print('==== Multiplication Table ====')
value = input('Type a number: ')
multiplier = 0
for multiplier in range(0, 11):
  print(f"{value} x {multiplier} = {int(value) * multiplier}")