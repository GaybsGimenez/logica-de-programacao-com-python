"""
Ordenação de elementos em uma lista, tupla ou conjunto.

Existem varias formas de ordenar elementos em uma lista, tupla ou conjunto.
bubble sort - ordena a lista em ordem crescente trocando os elementos de lugar, é um algortimo lento
sort() - ordena a lista em ordem crescente ou decrescente de forma mais eficiente que o bubble sort pois não troca os elementos de lugar 
e sim cria uma nova lista



# bubble sort: consiste em comparar cada elemento da lista com o seguinte, trocando-os de lugar se o segundo for menor que o primeiro.
o método bubble sort é um algoritmo lento, pois precisa percorrer a lista diversas vezes para ordená-la.

"""

# exemplo 6.20: ordenação pelo método bubble sort

# L é uma lista qualquer
L = [7, 4, 3, 12, 8]
# fim é a posição final da lista
fim = 5

# enquanto fim for maior que 1
while fim > 1:
    # trocou é uma variável booleana que indica se ocorreu uma troca na última passada pelo loop, é False no início de cada loop, pois ainda não ocorreu nenhuma troca
    trocou = False
    # x é uma variável que percorre a lista, é inicializada com 0 pois a lista começa na posição 0. 
    x = 0
    # enquanto x for menor que fim - 1, ou seja, enquanto x for menor que a posição final da lista - 1 (n-1), sendo n o tamanho da lista. 
    while x < (fim - 1):
        # se o elemento da posição x for maior que o elemento da posição x + 1, ou seja, se o elemento da posição x for maior que o elemento seguinte
        if L[x] > L[x + 1]:
            # troca os elementos de lugar
            trocou = True
            # temp é uma variável temporária que armazena o elemento da posição x
            temp = L[x]
            # o elemento da posição x recebe o elemento da posição x + 1
            L[x] = L[x + 1]
            # o elemento da posição x + 1 recebe o elemento da posição x
            L[x + 1] = temp
        # incrementa x para que o loop continue até o fim da lista e a lista seja ordenada
        x += 1
    # se não ocorreu nenhuma troca na última passada pelo loop, ou seja, se a lista está ordenada, o loop é interrompido
    if not trocou:
        break
    # -= significa que fim recebe fim - 1, ou seja, fim é decrementado em 1, serve para que o loop não percorra a lista inteira, pois o último elemento já está ordenado
    fim -= 1
# para cada elemento e na lista L
for e in L:
    # imprime o elemento
    print(e)


"""
# exercicio 6.14. O que acontece quando a lista já está ordenada? Rastreie o programa anterior, mas com a lista  L = [1, 2, 3, 4, 5].
Resposta: quando a lista já está ordenada, o loop while fim > 1 é executado apenas uma vez, pois o valor de fim é decrementado em 1 a cada passada pelo loop. ou seja, 
o loop while fim > 1 é executado 4 vezes, pois o valor de fim é decrementado em 1 a cada passada pelo loop.


# exercicio 6.15. O que acontece quando dois valores são iguais? Rastreie o programa anterior, mas com a lista  L = [3, 3, 1, 5, 4].
Resposta: quando dois valores são iguais o valores são trocados de lugar, indepentente da ordem em que aparecem na lista.


# exercicio 6.16 Modifique o programa anterior para ordenar a lista em ordem DECRESCENTE. L = [1, 2, 3, 4, 5] deve ser ordenada como [5, 4, 3, 2, 1].
Resposta: para ordenar a lista em ordem decrescente, basta trocar a condição do if L[x] > L[x + 1] para L[x] < L[x + 1], pois se o elemento da posição x for menor que o elemento da posição x + 1, os elementos são trocados de lugar.
"""    

# SORT() - ordena a lista em ordem crescente ou decrescente de forma mais eficiente que o bubble sort pois não troca os elementos de lugar e sim cria uma nova lista é MAIS EFICIENTE QUE O BUBBLE SORT

# exemplo 6.21: ordenação pelo método sort()

# L é uma lista qualquer
L = [7, 4, 3, 12, 8]
# .sort é um método que ordena a lista em ordem crescente, métodos são funções que pertencem a um objeto, no caso, o objeto é a lista L
L.sort()
# para cada elemento e na lista L
for e in L:
    # imprime o elemento
    print(e)
    
# Se desejar ordenar uma lista, sem alterar seus elementos, pode-se usar a função sorted().
# exemplo 6.22: ordenação pelo método sorted()
 
# Z é uma lista qualquer
Z = [7, 4, 3, 12, 8]
# sorted() é uma função que ordena a lista em ordem crescente, sorted() é uma função que não altera a lista original, mas cria uma nova lista ordenada
sorted(Z)

# se imprimir a lista Z, ela não estará ordenada, pois a função sorted() não altera a lista original. para ter acesso a lista ordenada, é necessário atribuir a lista ordenada a uma variável
# exemplo 6.23: ordenação pelo método sorted() atribuindo a lista ordenada a uma variável

# Z é uma lista qualquer
Z = [7, 4, 3, 12, 8]
# Z_ordenada recebe a lista Z ordenada
Z_ordenada = sorted(Z)