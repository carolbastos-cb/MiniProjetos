# encontrar o maior valor de uma lista
# solução 1

# lista
numeros = [7, 3, 9, 1, 2, 30, 6]

# definir um variável para guardar o maior valor e comparar os demais valores com esse valor
num = numeros[0]

# definir um variável para guardar o índice
i_num = 0

# iterar sobre os valores da lista
# nesse caso acessamos direto os valores da lista e precisamos da função index para descobrir o índice de cada elemento
for i in numeros: # para cada valor da lista
    if i > num: # se o valor da atual da lista for maior que o valor de num
        num = i # atualizar o valor de num com o valor atual da lista
        i_num = numeros.index(i) # atualizar o valor do índice com o índice atual da lista

print(f'O maior valor encontrado na lista é o número {num} e ele ocupa o índice {i_num}.')
