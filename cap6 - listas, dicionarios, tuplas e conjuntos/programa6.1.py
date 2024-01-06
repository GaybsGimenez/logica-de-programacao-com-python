#programa6.1 - cálculo de média aritmética
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"média: {soma/ x:5.2f}")

#programa6.2 - calculo da media com notas digitadas

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"nota {x}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"nota {x}: {notas[x]:6.2f}")
    x+=1
print(f"média: {soma/x:5.2f}")
