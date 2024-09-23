#programa 4.6 Categoria x preço Faça um programa que que leia a categoria de um produto e determine o preço pela tabela4.1
cat1 = 10
cat2 = 18
cat3 = 23
cat4 = 16
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
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
                if categoria == 4:
                    preco = 26
                else:
                    if categoria == 5:
                        preco = 31
                    else:
                        print("Categoria inválida, digite um valor entre 1 e 5!")
                        preco = 0
print(f"o preço do produto é R${preco:6.2f}")



  
    
