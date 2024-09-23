#programa_pag87 Imprimir apenas os numeros pares entre 0 e o numero digitado pelo usuario.

fim = int(input("digite o ultimo numero a imprimir: "))
x=0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x=x+1

#sem usar o if

fim = int(input("digite o ultimo numero a imprimir: "))
x=0
while x <= fim:
    print(x)
    x = x + 2
