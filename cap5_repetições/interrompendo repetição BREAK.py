#interrompendo repetição BREAK
s = 0
while True:
    v = int(input("Digite um número para somar ou digite zero (0) para sair: "))
    if v == 0:
        break
    s+=v
print(s)

#Escreva um programa que leia números inteiros do teclado. O programa deve ler os numeros até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritimética.
soma = 0
qte = 0

while True:
    n = int(input("digite um numero inteiro: "))
    if n == 0:
        break
    else:
        soma = soma + n
        qte = qte + 1
print("Quantidade de números digitados:", qte)
print("Soma: ", soma)
print(f"Média: {soma/qte:10.2f}")
