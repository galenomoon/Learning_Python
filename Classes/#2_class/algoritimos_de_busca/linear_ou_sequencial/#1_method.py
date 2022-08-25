import random

def execute_linear_search(array, value):
  for item in array:
    if value == item:
      return True
  return False

array = random.sample(range(100), 20)
number = input('Type a number: ')
print(sorted(array))
print(f"Is {number} in list? => {execute_linear_search(array, int(number))}")