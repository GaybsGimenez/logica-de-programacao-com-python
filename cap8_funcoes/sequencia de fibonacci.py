"""
a sequencia de fibonacci pode ser entendida como o numero de casais de coelhos que teríamos após cada ciclo de reprodução, considerando que 
cada ciclo da origem a um novo casal de coelhos e que cada casal de coelhos leva um ciclo para amadurecer e começar a reproduzir.

a sequencia de fibonacci é uma sequencia de numeros inteiros, começando por 0 e 1, na qual cada termo subsequente corresponde a soma
dos dois anteriores.

fibonacci = n
            fibonacci(n-1) + fibonacci(n-2) 
            
n<=1

"""
# função recursiva para a sequencia de fibonacci	

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# execicios de fixação

# defina uma funão recursiva que calcule o maior divisorcomum entre 2 numeros a e b, em que a > b

def mdc(a,b):
    if b == 0:
        return a 
    else:
        return mdc(b, a % b)

# usando a funao mdc defina no exercicios uma funcao para calcular o menor multiplo comum mmc entre dois numeros    
def mmc(a, b):
    return a * b // mdc(a, b)

# reescreva a funão do calculo de fibonacci sem usar recursao

def fibonacci_sem_recursao(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b 