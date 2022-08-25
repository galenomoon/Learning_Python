# Encontra o item no meio da sequência (meio da lista).
# Se o valor procurado for igual ao item do meio, a busca se encerra
# Se não for, checa se o valor buscado é MAIOR ou MENOR que o valor central
# Se for maior/menor, descarta a metade menor/maior e realiza a busca na restante, e assim sucessivamente

def binary_search(array, value):
    min = 0
    max = len(array) - 1
    while min <= max:
        # Encontra elemento que divide a lista ao meio
        center = (min + max)//2
        print(center)
        # Verifica se o valor procurado está à esquerda ou à direita do valor central
        if value < array[center]:
            max = center - 1
        if value > array[center]:
            max = center + 1
        else:
            return True  # Se o valor foi encontrado, para aqui
    return False  # Se o valor não foi encontrado, para aqui

array = list(range(1, 200))
number = input('Type a number: ')
print(f"\nIs {number} in list? => {binary_search(array, int(number))}")