#programa4.3 calculo do imposto de renda
salario = float(input("digite o salario para o calculo o IR: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base-3000)+0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"salario: R${salario:6.2f} IR a pagar: R${imposto:6.2f}")
