#exercicios_pag105_cap6
#exercicio6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
"""
lista1 = []
lista2 = []
while True:
    e = int(input("digite um número para lista 1, ou zero para finalizar : "))
    if e == 0:
        break
    lista1.append(e)
while True:
    e = int(input("digite um número para a lista 2, ou zero para finalizar : "))
    if e == 0:
        break
    lista2.append(e)

lista3 = lista1[:] #cópia dos elementos da lista1
lista3.extend(lista2)
x = 0
while x < len(lista3):
    print(lista3)
    x += 1
"""

#exercicio6.3 Fala um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
lista1 = []
lista2 = []
while True:
    e = int(input('digite um número para a lista1, ou zero para sair: '))
    if e == 0:
        break
    lista1.append(e)

while True:
    e = int(input('digite um número para a lista2, ou zero para sair: '))
    if e == 0:
        break
    lista2.append(e)

lista3 = []
posicao_lista_1 = 0
while posicao_lista_1 < len(lista1):
    elemento_lista1 = lista1[posicao_lista_1]
    posicao_lista_2 = 0
    repetiu = False
    while posicao_lista_2 < len(lista2):
        elemento_lista2 = lista2[posicao_lista_2]
        if elemento_lista1 == elemento_lista2:
            repetiu = True
            break
        posicao_lista_2 = posicao_lista_2 + 1
    if repetiu == False:
        lista3.append(elemento_lista1)
    posicao_lista_1 = posicao_lista_1 + 1

posicao_lista_1 = 0
while posicao_lista_1 < len(lista2):
    elemento_lista1 = lista1[posicao_lista_1]
    posicao_lista_2 = 0
    repetiu = False
    while posicao_lista_2 < len(lista1):
        elemento_lista2 = lista2[posicao_lista_2]
        if elemento_lista1 == elemento_lista2:
            repetiu = True
            break
        posicao_lista_2 = posicao_lista_2 + 1
    if repetiu == False:
        lista3.append(elemento_lista2)
    posicao_lista_1 = posicao_lista_1 + 1

print(lista3)









    
    
