"""
Aplicações

selecionar os elementos de um lista de forma a copia-los para outras duas listas. 

Imagine que os valores estejam inicialmente em uma lista V, mas que devam ser copiados para uma lista P, se forem pares, ou para uma lista I, se forem imprares

    
"""

# exercicio 1: copia de elementos para outras listas

V = [1,2,3,4,5,6,7,8,9,10]
P = []
I = []

for e in V:
    if e % 2 ==0:
        P.append(e)
    else:
        I.append(e)

print("Lista V: ", V)
print("Pares: ", P)
print("Impares: ", I)

# programa que controla a utilização das salas de um cinema. Imagine que a lista de lugares_vagos = [10,2,1,3,0] indica a quantidade de lugares vagos nas salas 1, 2, 3, 4, e 5, respectivamente.
# Esse programa lerá o numero de sala e a quantidade de lugares solicitados, ou seja, se ainda ha lugares livres. 
# caso seja possivel vender os bilheres, utilizará o numero de lugares livres
# a saida ocorre quando digita "0"

# programa 6.13 controle de utilização de salas de cinema

# lista de lugares vagos
lugares_vagos = [10,2,1,3,0] # lista de lugares vagos

# loop infinito
while True:
    # mostra as salas e suas quantidades de lugares vagos
    sala = int(input("Sala (0 sai): "))
    # sai do loop se digitar 0
    if sala == 0:
        print("Fim")
        break
    # se digitar um numero de sala invalido ou maior que o numero de salas, mostra a mensagem
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala invalida")
    # então, sala é valida, mas esta lotada e mostra a mensagem
    elif lugares_vagos[sala-1] == 0:
        print("Desculpe, sala lotada!")
    # senão, ha lugares vagos, entao pede quantos lugares o usuario deseja
    else:
        lugares = int(input("Quantos lugares você deseja ({lugares_vagos[sala-1]} vagos:"))
        # se o numero de lugares for maior que o numero de lugares vagos, mostra a mensagem
        if lugares > lugares_vagos[sala-1]:
            print("Esse numero de lugares não esta disponivel.")
        # se então, o numero de lugares for menor que zero, mostra a mensagem
        elif lugares < 0:
            print("Numero invalido")
        # senão, vende os bilhetes, ou seja, diminui o numero de lugares vagos
        else:
            lugares_vagos[sala-1] -= lugares
            print(f"{lugares} lugares vendidos")
            
# mostra a utilização das salas
print("Utilização das salas")
# percorre a lista de lugares vagos
for x,l in enumerate(lugares_vagos):
    # mostra a quantidade de lugares vagos
    print(f"Sala {x+1} - {l} lugares vagos")
    

    