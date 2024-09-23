"""
Funções são usadas quando queremos reutilizar um código, ou seja, quando queremos que um mesmo código seja executado várias vezes.
Geralmente, quando esse código é executado, ele recebe um valor diferente, e retorna um resultado diferente.

Um problema classico de programação é o calculo do fatorail. O fatorial de um número é o produto dele por todos os seus antecessores, 
até o 1. Por exemplo, o fatorial de 5 é 5*4*3*2*1, ou seja, 120.

O fatorial de um numero é utilizado em estatistica para calcular o numero de combinações e permutações de conjuntos. 

"""
# calculo fatorial

# definindo a função fatorial que vai receber apenas um parâmentro, que é o número que queremos calcular o fatorial.
def fatorial(n):
    # definindo a variável fat, que vai receber o valor 1, pois o fatorial de 1 é 1.
    fat = 1
    # enquanto o valor de n for maior que 1, o valor de fat vai ser multiplicado por n, e n vai ser decrementado em 1.
    while n > 1:
        # fat = fat * n ou seja, a variavel fat vai receber o valor dela mesma multiplicado por n.
        fat = fat * n
        # n = n - 1 ou seja, a variavel n vai receber o valor dela mesma menos 1.
        n = n - 1 
        # retornando o valor de fat.
        return fat

# O calculo do fatorial foi multiplicando o valor de N pelo valor anteior (fat), e começamos do maior numero até chegar no 1.

# Calculo do fatorial de zero

# definindo a função fatorial que vai receber apenas um parâmentro, que é o número que queremos calcular o fatorial.
def fatorial(n):
    # definindo a variável fat, que vai receber o valor 1, pois o fatorial de 1 é 1.
    fat = 1
    # x é uma variavel que vai receber o valor 1, pois o fatorial de 1 é 1.
    x = 1 
    # enquanto o valor de x for menor ou igual a n, o valor de fat vai ser multiplicado por x, e x vai ser incrementado em 1.
    while x <= n:
        # fat = fat * x ou seja, a variavel fat vai receber o valor dela mesma multiplicado por x.
        fat = fat * x
        # x = x + 1 ou seja, a variavel x vai receber o valor dela mesma mais 1.
        x = x + 1
        
# Exercicio: Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesqisa em lista, vistos no Capítulo 7.

# definindo a função pesquisa que vai receber dois parâmetros, uma lista e um valor.
def pesquisa(lista, valor):
    # se o valor estiver na lista, retorna o indice do valor na lista.
    if valor in lista:
        # retorna o indice do valor na lista. .index() significa que vai retornar o indice do valor na lista.
        return lista.index(valor)