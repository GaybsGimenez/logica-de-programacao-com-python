#programa4.7 - categoria x preco, usando elif.py
cat1 = 10
cat2 = 18
cat3 = 23
cat4 = 26
cat5 = 31

def tabela4():
    print("categoria\t\preço")
    print("-------------------------------------")
    print("%s:\t\t\t%f" %(cat1, 10))
    print("%s:\t\t\t%f" %(cat2, 18))
    print("%s:\t\t\t%f" %(cat3, 23))
    print("%s:\t\t\t%f" %(cat4, 26))
    print("%s:\t\t\t%f" %(cat5, 31))
    print("-------------------------------------")

tabela4()

categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("categoria inválida, digite um valor entre 1 e 5!")
    preco = 0
print(f"o preco do produto pe R${preco:6.2f}")
