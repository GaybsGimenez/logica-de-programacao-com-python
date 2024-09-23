"""
RANGE

Podemos utilizar o RANGE  para GERAR listas simples. A função range não retorna uma lista, mas sim um gerador de números.

Exemplo1:        

for v in range(10):
    print(v)

a função range gera numeros de 0 a 9, ou seja, 10 elementos. pois passamos 10 como parametro. normalmente gera valores de 0 a n-1
vantagem de usar o RANGE, é que apenas um valor é armazenado na memória, e não uma lista inteira.

Exemplo2: 
podemos indicar em qual elemento começar e em qual terminar.

for x in range(5, 8):
    print(x)

Retornará 5, 6, 7, pois inicia no 5 até n-1, ou seja 8-1 = 7. 

Exemplo3:
Acrescentando um 3 elemento, podemos indicar o passo, ou seja, de quanto em quanto queremos que o range pule.

for i in range(3 ,33, 3):
    print(i, end=' ')

retornará 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

OBERSVAÇÃO: Função especial no print, end=' ', que indica que o print não quebra a linha, e sim coloca um espaço entre os valores.

O gerador como retornado pela função range, pode ser convertido em uma lista, utilizando a função list(). MAS NÃO É UMA LISTA, E SIM UM OBJETO GERADOR.

exemplo4:
# programação 6.10 -  tranformação de range em uma lista

L = list(range(100, 1100, 50))
print(L)

    
"""
Z = list(range(2, 10, 2))
print(Z)

# Retorna uma lista, pois foi convertido em lista, e não um gerador.  a lista z = [2, 4, 6, 8], pois inicia no 2, e vai até o 10-1, e pula de 2 em 2.

a = [5, 9, 13]
x = 0
for e in a:
    print(f'[{x}] {e}')
    x += 1

# retorna a lista a, com os indices, pois foi criado uma variavel x, e incrementado a cada iteração. ou seja, x = 0, x = 1, x = 2.

for x, e in enumerate(a):
    print(f'[{x}] {e}')

# retorna a lista a, com os indices, pois foi criado uma variavel x, e incrementado a cada iteração. ou seja, x = 0, x = 1, x = 2.