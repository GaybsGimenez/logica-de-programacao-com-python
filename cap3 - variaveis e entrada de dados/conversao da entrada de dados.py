#conversao de entrada de dados
anos = int(input("anos de serviço: "))
valor_por_ano = float(input("valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R${bonus:5.2f}")
