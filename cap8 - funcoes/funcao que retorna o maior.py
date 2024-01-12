"""
Escreva uma função que retorne o maior de dois números.
valores esperados:
maximo(5, 6) == 6
maximo(2, 1) == 2
maximo(7, 7) == 7
"""

def maximo(a, b):
    if a > b:
        return a
    else:
        return b

print(maximo(5, 6))
print(maximo(2, 1))
print(maximo(7, 7))

"""
Escreva uma função que receba dois numeros e retorne True se o primeiro número for múltiplo do segundo.
valores esperado
multiplo(8, 4) == True
multiplo(7, 3) == False
multiplo(5, 5) == True

"""

def multiplo(a, b):
    return a % b == 0

print(multiplo(8, 4))  
print(multiplo(7, 3))
print(multiplo(5, 5))

"""
Escreva uma função que receba o lado de uma quadrado e retorne sua área (A = lado²).
valores esperados:
area_quadrado(4) == 16
area_quadrado(9) == 81

"""

def area_quadrado(lado):
    return lado ** 2 # ou lado * lado 

print(area_quadrado(4))
print(area_quadrado(9))

"""
Escreva uma função que receba a base e a altura de um triangulo e retorne sua área (A = (base * altura) / 2).
valores esperados:
area_triangulo(6, 9) == 27
area_triangulo(5, 8) == 20

"""

def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_triangulo(6, 9))
print(area_triangulo(5, 8))

