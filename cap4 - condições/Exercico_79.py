#Exercico_79
#4.3 Escreva um programa que leia tres numeros e que imprima o maior e o menor
n1 = int(input("escreva um numero inteiro: "))
n2 = int(input("escreva um numero inteiro diferente do anterior: "))
n3 = int(input("escreva um numero inteiro diferente dos dois anteriores: "))

if n1 > n2:
    if n1 > n3:
        print(f"o numero maior é {n1}")

if n2 > n1:
    if n2 > n3:
        print(f"o numero maior é {n2}")

if n3 > n1:
    if n3 > n2:
        print(f"o numero maior é {n3}")


#4.4 Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento. Para salarios superiores a R$1250,00, calcule um aumento de 10%. para inferiores ou iguais, de 15%.

salario = float(input("Qual o seu salário: "))
base = salario
aumento = 0
if base > 1250:
    aumento = aumento + (base * 0.10) + salario
    base <= 1250
if base <= 1250:
    aumento = aumento + (base * 0.15) + salario

print(f"o aumento para o salario de R${salario:6.2f} é de R${aumento:6.2f} reais")
    
