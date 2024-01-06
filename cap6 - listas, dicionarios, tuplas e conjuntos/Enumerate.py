"""
Com a funão ENUMERATE() podemos enumerar elementos de uma lista. 

"""

# Exemplo1: ampliar as funcionalidades do for
L = ['a', 'b', 'c', 'd', 'e']
x = 0
for i in L:
    print(f'[{x}] = {i}')
    x += 1

# Temos uma lista L e queremos imprimir o indice e o valor de cada elemento. ou seja, queremos imprimir: L=[0] = a, L=[1] = b, L=[2] = c, L=[3] = d, L=[4] = e

# Exemplo2: usando a função enumerate()

L = ['a', 'b', 'c', 'd', 'e']
for x, i in enumerate(L):
    print(f'[{x}] = {i}')

# A função enumerate() retorna uma tupla com o indice e o valor do elemento. ou seja (0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')