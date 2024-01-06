#ex5.15_cap5_pa92 Escreva um programa para controlar uma pequena paquina registradora. voce deve solicitar ao user que digite o cog do produto e a quantidade comprada.
#Seu programa deve exibir o total das compras depois que o usuario digitar O. Qualquer outro código deve gerar uma msg de erro "código inválido".

apagar = 0
while True:
    cod = int(input("digite o código do produto: "))
    preco = 0
    if cod == 0:
        break
    elif cod == 1:
        preco = 0.5    
    elif cod == 2:
        preco = 1    
    elif cod == 3:
        preco = 4    
    elif cod == 5:
        preco = 7    
    elif cod == 9:
        preco = 8
    else:
        print("código inválido")
    if preco != 0:
        qte = int(input("Quantidade: "))
        apagar = apagar + (preco * qte)
print(f"Total a pagar R${apagar:8.2f}")

