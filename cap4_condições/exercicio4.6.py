#exercicio4.6 Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando o R$0,50 por km para viagens de até de 200km, e R$0,45 para viagens mais longas.
distancia = int(input("qual a distancia que pretende percorrer: "))

if distancia <= 200:
    passagem = distancia*0.50
else:
    passagem = distancia*0.45

print(f"o valor da passagem é {passagem:6.2f} reais")


