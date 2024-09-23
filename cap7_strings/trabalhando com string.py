"""
    - Strings são imutáveis, mas podemos acessar strings e fatiar strings para criar novas strings como listas

"""
S = "Alô mundo"
print(S[0])
print(S[1])

# Retorna A

S[0] = "a"
# Retorna erro, pois strings são imutáveis ou seja, não tem como alterar uma string.
#typeError: 'str' object does not support item assignment

"""
trabalhar com caractere a caractere com uma string, alterando seu valor, teremos que converter a string em uma lista

"""

#exemplo

L = list(S) # função list() converte uma string em uma lista
L[0] = "a"
print(L)
# Retorna ['a', 'l', 'ô', ' ', 'm', 'u', 'n', 'd', 'o'] com o primeiro caractere alterado de "A" para "a"

s = "".join(L) # "".join() junta os elementos da lista em uma string, tudo que vem antes do ponto final é 
# o que será usado para juntar os elementos da lista, no caso, nada, então os elementos serão juntados sem nada(sem espaços) entre eles.
print(s)
# retorna "alô mundo"
