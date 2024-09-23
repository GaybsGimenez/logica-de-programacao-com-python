#exercicios_cap5_pag88

#ex5.6 Altere o programa para exibir os resultados no mesmo formato de uma tabuada : 2x1=2...
n = int(input("tabuada de: "))
x = 1
while x <=10:
    r =(n*x)
    x=x+1
    print(f"{n} x {x-1} = {r}")

#ex5.7 modifique o programa anterior de forma que o usuario tambpem digite o inicio e o fim da tabuada em vez de começar com 1 e 10.
n = int(input("tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n*x}")
    x=x+1

#ex5.8 Escreva um programa que leia dois numeros. imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois numeros como a soma sucessiva de um deles. assim: 4x2 = 2 + 2 + 2 + 2.
n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
x = 1
r = 0
while x <= n2:
    r = r + n1
    x = x + 1
print(f"{n1} x {n2} = {r}")

#ex5.9 escreva um prog que leia dois numeros. imprima a divisão inteira do primeiro pelo segundo, assim com oo resto da divisão. utilize apenas os operadores de soma e subtração para calcular o resultado.
n1 = int(input("digite o primeir numero: "))
n2 = int(input("digite o segundo numero: "))
quociente = 0
x = n1
if n2 <= 0:
    print("da matemática não existe divisão por zero, escolha outro numero: ")
else:
    while x >= n1:
        x = x - n2
        quociente = quociente + 1
    resto = x
    print(f"{n1}/{n2} = {quociente} (quociente) {r} (resto)")
    
        
    

