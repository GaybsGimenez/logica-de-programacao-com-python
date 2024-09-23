"""
Listas podem ser percorridas    

    
"""
# Exemplo1: verificar o maior valor

L = [8, 9, 15, 20, 3, 5, 7, 1, 2, 4, 6, 10, 11, 12, 13, 14, 16, 17, 18, 19]
maximo = L[0]
for e in L:
    if e > maximo:
        maximo = e
print(maximo)

# retornará 20, pois a cada linha ele compara o valor de e com o valor de maximo, se e for maior que maximo, maximo passa a ser o valor de e

# Exercicio 6.12 : altere o programa 6.11 de forma a imprimir o menos elemento da lista

L = [8, 9, 15, 20, 3, 5, 7, 1, 2, 4, 6, 10, 11, 12, 13, 14, 16, 17, 18, 19]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)

# retornara 1, pois a cada linha ele compara o valor de e com o valor de minimo, se e for menor que minimo, minimo passa a ser o valor de e

# exercicio 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]
max = L[0]
min = L[0]
med = L[0]

for e in T:
    if e > max:
        max = e
    elif e < min:
        min = e
    else:
        media = (max + min) / 2

print('A maior temperatura é: ', max)
print('A menor temperatura é: ', min)
print('A temperatura média é: ', media)
    