"""
Verificar se uma string começa ou termina com algum caractere. usar o método startswith() e endswith() respectivamente. 
Esses metodos retornam True ou False


"""

# verificar se uma lista de string começa com maiuscula ou minuscula. usando startswith(). 

L = ["Alô mundo", "Olá mundo", "alô mundo", "olá mundo"]
for string in L:
    if string.startswith("a"):
        # se a string começar com "A" minusculo, mudar para maiusculo
        print(string.capitalize()) # capitalize() deixa a primeira letra da string maiuscula
    else:
        print(string)
        
# usando While, quando não se sabe o tamanho da lista e nem quais elementos ela contem.

# L é uma lista de strings
L = ["Alô mundo", "Olá mundo", "alô mundo", "olá mundo"]
# i é um contador, ele é usado para percorrer a lista e iniciar no indice 0
i = 0
# enquanto i for menor que o tamanho da lista L
while i < len(L):
    # se o primeiro elemento da lista L for minusculo
    if L[i][0].islower():
        # deixar a primeira letra maiuscula
        print(L[i].capitalize())
    # se não
    else:
        # imprimir a string
        print(L[i])
    # incrementar o contador ou sejna i = i + 1 (i += 1)   
    i = i + 1
    
s = "O Rato roeu a roupa do rei de Roma"
s.lower()
# 'o rato roeu a roupa do rei de roma'
s.upper()
# 'O RATO ROEU A ROUPA DO REI DE ROMA'
s.capitalize()
# 'O rato roeu a roupa do rei de roma'
s.title()
# 'O Rato Roeu A Roupa Do Rei De Roma'
s.swapcase()
# 'o rATO ROEU A ROUPA DO REI DE rOMA'
s.count("r")
# 3
s.lower().startswith("o rato") # quando usamos a função lower() com o startswith() 
# temos que colocar a string que queremos verificar. essa tecnica é chamada de encadeamento de metodos, ou seja, 
# um metodo encadeado no outro. verificamos se a string começa com "o rato"  e minusculo.
# True
s.lower().endswith("roma")
# True

# O que é colocar como argumento de uma função um metodo de uma string?
# é o mesmo que fazer isso:
s = "O Rato roeu a roupa do rei de Roma"
s.lower().startswith("o rato")
# True
# é o mesmo que fazer isso:
s = "O Rato roeu a roupa do rei de Roma"
s = s.lower()
s.startswith("o rato")
# True

#Essa abordagem permite que você generalize funções para trabalhar com diferentes métodos de 
# string sem alterar a função principal. Isso é útil em situações em que você deseja fornecer flexibilidade na manipulação de strings,
# permitindo que o usuário da função escolha o método a ser aplicado.