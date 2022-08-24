import random

def shuffler(words): 
 array = list(words)
 random.shuffle(array)
 return '/'.join(array)

print("==== Sorteio Do Jogo da Wikipedia ====")
words_length = input("Quantas rodadas terão?: ")
i = 0
words = []
while i < (int(words_length) * 2):
  palavra = input(f'{i+1}ª palavra: ')
  words.append(palavra)
  i = i+1
print('--------PALAVRAS SORTEADAS-----------')
print(shuffler(words))