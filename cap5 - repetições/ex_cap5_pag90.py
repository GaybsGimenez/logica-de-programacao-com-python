#ex_cap5_pag90
#ex5.11 Escreva um programa que pergunte o deósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para o s24 primeiros meses. Escreva o total danho com kuros período.
deposito = float(input("Depósito inicial: "))
juros = float(input("taxa de juros: "))
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (juros/100))
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f"ao final de tods os meses, o juros em conta é de R${saldo-deposito:5.2f}.")



#ex5.12 Altere o programa anterior de forma a perguntar tambem o valor depositado mensalmente. Esse valor sera depositado no inicio de cada mes, e você deve considera-lo para calculo de juros do mes seguinte.

deposito = float(input("Depósito inicial: "))
juros = float(input("taxa de juros: "))
deposito_mensal = float(input("Depósito mensal: "))
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (juros/100)) + deposito_mensal
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f"ao final de tods os meses, o juros em conta é de R${saldo-deposito:5.2f}.")

#ex5.13 Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que dívida seja paga,o total pago e o total de juros pago.
divida = float(input("valor inicial da dívida: "))
taxa = float(input("taxa de juros mensal: "))
pagto_mensal = float(input("pagamento mensal no valor de  R$: "))
mes = 1
if (divida * (taxa/100) > pagto_mensal):
    print("Escolha outra valor de pagamento, pois os juros são superiores ao pagamento mensal.")

else:
    saldo = divida
    juros_pago = 0
    while saldo > pagto_mensal:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagto_mensal
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}.")
        mes = mes + 1
    print(f"Para pagar uma dívida de R${divida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")
