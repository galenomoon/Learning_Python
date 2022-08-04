import random

def shuffler(word): 
 array = list(word)
 random.shuffle(array)
 return ''.join(array).upper()

print("==== String Shuffler ====")
word = input("Type a word: ")
print(f'Your shuffled word is: {shuffler(word)}')