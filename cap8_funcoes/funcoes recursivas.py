"""
funções recursivas são funções que chamam a si mesmas. 

# problema do fatorial
Podemos definr o fatorial de um numero como sendo esse numero multiplicado pelo fatorial do número anterior.
Se chamarmos nosso numero de n, podemos definir o fatorial de n como sendo n * (n-1) * (n-2) * ... * 1

 fatorial(n) = 1
               n * fatorial(n-1) 
               
0<=n<=1


"""

#programa função recursiva do fatotial

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)
    
# função modificada para facilitar o rastreamento

def fatorial(n):
    print(f"calculando o fatorial de {n}")
    if n == 0 or n==1:
        print(f"fatorail de {n} é = 1")
        return 1
    else:
        fat = n * fatorial(n-1)
        print(f"fatorial de {n} é {fat}")
    return fat

# exemplo de uso
print(fatorial(5)) # 120