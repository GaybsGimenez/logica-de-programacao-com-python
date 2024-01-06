#programa6.3 - apresentação de números
#programa lê 5 numeros , armazena-os em uma lista e depois solicita ao usuário que escolha um numero a mostrar

numero = [0, 0, 0, 0, 0]
x=0
while x < 5:
    numero[x] = int(input(f"digite um numero {x+1}: "))
    x+=1
while True:
    escolhido = int(input("que posição vc qie imprimir (0 para sair): "))
    if escolhido == 0:
        break
    else:
        print(f"vc escolheu o número: {numero[escolhido - 1]}")
