#exercicio_cap5_pag87

#exercicio 5.4 Modifique o programa anterior para imprimir de 1 até o numero digitado pelo usuário, mas dessa vez, apenas os ímpares. ISANDO IF
fim = int(input("digite o ultimo numero: "))
x=0
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x+1

#reescreva o programa anterior para escrever os 10 primeiros multiplos de 3:
fim = int(input("digite o ultimo numero: "))
x=0
while x <= fim:
    print(x)
    x = x+3

#imagine ter de imprimir a tabuada de adição de um numero digitado pelo usuario.Essa tabuada deve ser impressa de 1 a10, sendo "n" o numero digitado pelo user.
n = int(input("tabuada de: "))
x = 1
while x <=10:
    print(n*x)
    x=x+1
