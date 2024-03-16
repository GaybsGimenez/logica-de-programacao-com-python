'''

Em python é muito simples gerar arquivos, por exemplo o programa a seguir, 
que gera dois arquivos com 500 linhas cada. O programa distribui os números impares e pares em arquivos diferentes


'''

# gravaçãio de numeros impares e pares em arquivos diferentes
with open('impares.txt', 'w') as impares:
    with open('pares.txt', 'w') as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")
                
# oberve que o programa utiliza dois blocos with, um para cada arquivo.
# o bloco with garante que o arquivo será fechado após a execução do bloco.
# o arquivo é aberto no modo de escrita (w) e o método write é utilizado para escrever no arquivo.
# o caractere \n é utilizado para pular para a próxima linha.
# para gravar em arquivos diferentes, utilizamos um if e dois arquivos abertos para escrita. 

# podemos escrever os WITH em um só, por exemplo:
with open('impares.txt', 'w') as impares, open('pares.txt', 'w') as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f"{n}\n")
        else:
            impares.write(f"{n}\n")
            
# L3ITURA E ESCRITA

# agora pegar oq ue foi gerado no arquivo pares.txt e filtra-lo de forma a gerar um novo arquivo, apenas com os numeros multiplos de 4.

# gerar um arquivo com os multiplos de 4 e abrir o arquivo pares.txt para leitura
with open('multiplos_de_4.txt', 'w') as multiplos4, open('pares.txt', 'r') as pares:
    # para cada linha no arquivo pares.txt
    for linha in pares.readlines():
        # se a linha for multiplo de 4, 
        if int(linha) % 4 == 0:
            # escreva a linha no arquivo multiplos4.txt
            multiplos4.write(linha)