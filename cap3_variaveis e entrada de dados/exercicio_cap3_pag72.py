#exercicio_cap3_pag72
#3.7 Fça um programa que peça dois numeros inteiros. Imprima a soma desses dois numeros na tela
n1 = float(input("digite um número: "))
n2 = float(input("digite outro número: "))
soma = n1+n2
print(f"A soma dos números é: {soma}")


#exercicio3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

v_metro = float(input("escreva um valor em METROS: "))
milimetro = (v_metro * 1000)
print(f"valor em milimetro é {milimetro}")

#exercicio3.9 Escreva um programa que leia a quantidade de dias, horas,minutos e segundos do usuário. Calcule o total em segundos
dias = int(input("digite o dia: "))
horas = int(input(" digite a hora: "))
minutos = int(input("digite o minuto: "))
segundos = int(input("digite o segundo: "))
# 1 hora = 3600 segundos
# 1 dia = 24h
# 1 min = 60s
total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print(f"Convertido em segundos é igual a {total_segundos} segundos.")

#exercicio3.10 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e aporcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("digite o valor do salário atual: "))
aumento = float(input("digite a porcentagem de aumento: "))
valor_aumento = (salario * aumento/100)
salario_novo = valor_aumento + salario
print(f"O aumento foi de  {valor_aumento} e o salario novo agora é {salario_novo}")

#exercicio3.11 Faça um programa que solicite o preço de uma mercadoreia e o percentual de desconto. Exiba o valor do desconto e o preço da mercadoria.
mercadoria = float(input(" Valor da mercadoria: "))
desconto = int(input("percentual de desconto: "))
desconto_real = 100 - desconto
valor_novo_mercadoria = (mercadoria * desconto_real/100)
print(f"mercadoria custava {mercadoria}, com o desconto de {desconto}% porcento, passou a custar {valor_novo_mercadoria}.")


#exercicio3.12 Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distancia a percorrer e a velocidade média esperada para a viagem
distancia = int(input("Qual a distancia a percorrer em km: "))
vm = int(input("Qual a velocidade média em km/h: "))
tempo = distancia/vm
print(f" A duração da viagem em horas é de: {tempo}h")

#exercicio3.13 Escreva um programa que converta uma temperatura digitada em Celsius em fahrenheit
C = int(input("digite a temperatura em C: "))
F = (9*C/5) + 32
print(f" a temperatura em fahrenheit é de: {F}")

#exercicio3.14 Escreva um prog que pergunte a quantidade de km percorrido por um carro alugado pelo usuario, asim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e  R$15,00 por km rodado.
km_percorrido = int(input("Quantos km foram percorridos: "))
dias_alugado = int(input("Ficou alugado por quantos dias: "))
valor_dia = (60 * dias_alugado)
valor_km = (0.15 * km_percorrido)
a_pagar = valor_dia + valor_km
print(f"o preço do aluguel foi de R${a_pagar:5.2f} reais")

#exercicio3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
cigarros_dia = int(input("quantos cigarros você fuma por dia?: "))
anos_fumando = int(input("quantos anos você fuma?: "))
#1 hora = 60min
#24h = 1 dia
min_perdidos = anos_fumando * 365 * cigarros_dia * 10
dias_perdidos = min_perdidos / (24*60)
print(f"essa pessoa perdeu {dias_perdidos:5.2f} dias de vida.")



















