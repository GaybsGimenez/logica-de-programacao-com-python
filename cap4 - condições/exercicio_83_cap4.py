#exercicio_83_cap4

#4.8 Escreva um programa que leia dois numeros e que pergunte qual operacao voce deseja realizar. Voce deve poder calcular soma, subtração multiplicacao e divisao. Exiba o resultado da operação solicitada.

n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
operacao = input("Escreva o nome da operacao que deja fazer (+,-,* ou /): ") 


if operacao == "+":
    print(f"o resultado da soma é: {n1+n2}")
elif operacao == "*":
    print(f"o resultado da multiplicacao é: {n1*n2} ")
elif operacao == "-":
    print(f"o resultado da subtracao é: {n1-n2} ")
elif operacao == "/":
    print(f"o resultado da divisao é: {n1/n2} ")
    
else:
     print("operacao inválida!")
     resultado = 0

#4.9 Escreva um programa para aprovar o emprestimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a
#30% do salario. Calcule o valor da prestaççao como sendo o valor da casa a comorar dividido pelo numero de meses a pagar.

valor_imovel = float(input("Informe o valor do imóvel: "))
salario =  float(input("Informe o salário: "))
anos_pagar = int(input("Infome a quantidade de anos a pagar: "))

prestacao = valor_imovel/anos_pagar
valor_max_parcela = salario * 0.30

if prestacao < valor_max_parcela:
    print(f"financiamento aprovado, o valor da parcela será de R${prestacao:6.2f} reais.")
else:
    print(f"financiamento negado, valor da parcela de R$ {prestacao:6.2f} é maior que 30% do salário.")

#4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencias, I para industrias e C para comercio.
#Calcule o preço a pagar de acordo com a tabela a seguir:

faixa_kwh = float(input("Infome o valor do kWh consumido: "))
tipo_instalacao = input("Qual tipo de instalação? (R , I, C): ")

p1 = 0.40
p2 = 0.65
p3 = 0.55
p4 = 0.60
p5 = 0.55
p6 = 0.60

if tipo_instalacao == "R":
    if faixa_kwh <= 500:
       preco = 0.40
    else:
        preco = 0.65

elif tipo_instalacao == "I":
    if faixa_kwh <= 1000:
        preco =0.55
    else:
        preco = 0.60

elif tipo_instalacao == "C":
    if faixa_kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Inválido, coloque uma tipo de instação conhecida")

custo = faixa_kwh * preco
print(f"Preço a pagar é de R${custo:5.2f} reais.")



































