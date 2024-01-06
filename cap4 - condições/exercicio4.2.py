#exercicio4.2 Escreva um programa que pergunte a velocidade do carro de um usuario. Caso ultrapasse 80km\h, exiba uma msg dizendo que o usuário foi multado. Nesse cao, Exiba o valor da multa, cobrando R$5 por km acima de 80km\h
velocidade_carro = int(input("qual a velocidade do carro: "))
multa = (velocidade_carro - 80)*5
if velocidade_carro > 80:
    print(f"Você foi multado e sua multa é no valor de R${multa:5.2f} reais")
if velocidade_carro <= 80:
    print("você não foi multado")
    
