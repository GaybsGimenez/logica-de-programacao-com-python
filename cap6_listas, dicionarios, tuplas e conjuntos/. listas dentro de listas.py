"""
Podemos acessar as strings dentro de uma lista de listas usando dois colchetes e dois índices, o primeiro para a lista e o segundo para o item dentro dessa lista.

"""

# Exemplo: lista de listas
S = ["maça", "banana", "laranja", "pera", "uva", "manga", "goiaba", "abacaxi", "melancia", "melão"]

print(S[0][0]) #retorna o primeiro elemento da primeira lista S = 'm'
print(S[0][1]) #retorna o segundo elemento da primeira lista S = 'a'
print(S[0][2]) #retorna o terceiro elemento da primeira lista S = 'ç'
print(S[0][3]) #retorna o quarto elemento da primeira lista S = 'a'

# retornou cada caractere da primeira string da lista S 

# Exemplo: lista de listas

M = [["maça", "banana", "laranja", "pera", "uva", "manga", "goiaba", "abacaxi", "melancia", "melão"], ["maça", "banana", "laranja", "pera", "uva", "manga", "goiaba", "abacaxi", "melancia", "melão"], ["maça", "banana", "laranja", "pera", "uva", "manga", "goiaba", "abacaxi", "melancia", "melão"]]

print(M[0][0]) #retorna o primeiro elemento da primeira lista M = 'maça'
print(M[0][1]) #retorna o segundo elemento da primeira lista M = 'banana'
print(M[0][2]) #retorna o terceiro elemento da primeira lista M = 'laranja'

# retornou cada elemento da primeira lista da lista M

# Exercicio . - Impressão de uma lista de strings, letra por letra

L = ['maça', 'banana', 'laranja', 'pera', 'uva', 'manga', 'goiaba', 'abacaxi', 'melancia', 'melão']
for string in L:
    for letra in string:
        print(letra)

print(L[0][0]) #retorna o primeiro elemento da primeira lista L = 'm'
print(L[0][1]) #retorna o segundo elemento da primeira lista L = 'a'
print(L[0][2]) #retorna o terceiro elemento da primeira lista L = 'ç'


# exercicio 6.18 - impressao das compras

# produto1 é uma maça, com 10 unidades e custa 0.30
produto1 = ['maça', 10, 0.30]
# produto2 é uma banana, com 5 unidades e custa 0.75
produto2 = ['banana', 5, 0.75]
# produto3 é uma laranja, com 4 unidades e custa 0.80
produto3 = ['laranja', 4, 0.80]

# lista de compras
compras = [produto1, produto2, produto3]

# para cada produto na lista de compras, imprime o produto
for p in compras:
    print('Produto: %s' % p[0])
    print('Quantidade: %d' % p[1])
    print('Preço: %5.2f' % p[2])
    
    
"""
Da mesma forma, podemos acessar os preços do segundo elemento com 
compras[1][2] e o preço da laranja com compras[2][2].

"""

# exercicio 6.19 - criação e impressão da lista de compras

# lista de compras vazia para adicionar os produtos
compras = []

# enquanto o produto for diferente de fim, adiciona o produto, a quantidade e o preço na lista de compras
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    # digitar a quantidade de produtos
    quantidade = int(input('Quantidade: '))
    # digitar o preço do produto
    preco = float(input('Preço: '))
    # adiciona o produto, a quantidade e o preço na lista de compras
    compras.append([produto, quantidade, preco])
# a soma inicia de zero pois ainda não foi adicionado nenhum produto a medida que for adicionando os produtos, a soma vai aumentando
soma = 0.0
# para cada produto na lista de compras, imprime o produto, a quantidade, o preço e o total
for e in compras:
    print(f'{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}')
    # soma += significa soma = soma +. soma recebe o valor da soma mais o valor do produto vezes a quantidade
    soma += e[1] * e[2]
print(f'Total: {soma:7.2f}')

# retona o produto, a quantidade, o preço e o total