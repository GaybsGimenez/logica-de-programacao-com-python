"""
FUNÇÕES são blocos de código que podem ser executados em qualquer parte do programa, como len(), print(), etc. 
mas dá pra declarar funções também, como por exemplo:
def nome_da_funcao():
    # código da função
    return # opcional
    
OBS: o return é opcional, mas se não for declarado, a função retorna None
OBS: o return encerra a função, ou seja, se tiver um código depois dele, não será executado

Para definir uma função, é necessário usar a palavra reservada def, seguida do nome da função, parênteses e dois pontos.

"""
# Exemplo: função simples de soma

# difinir a função soma (a e b são parâmetros, ou seja, valores que serão passados para a função)
def soma(a, b):
    print(a+b) # imprime a soma de a e b

soma(1, 2) # chama a função com os valores 1 e 2 como parâmetros
soma(3, 4)

# Só retorna o valor, não imprime. para imprimir é necessário usar o print

def soma(a, b):
    return a+b
print(soma(1, 2))

# imprimerá 3, pois 1+2=3 

# Exemplo: Definir uma função retornar a par ou ímpar, dependendo do valor passado como parâmetro

def e_par(x):
    return x % 2 == 0 # retorna True se o resto da divisão de x por 2 for 0, ou seja, se x for par

def par_ou_impar(x):
    if e_par(x): # se x for par
        print("par")
    else:
        print("impar")
        
print(par_ou_impar(2))
print(par_ou_impar(3))