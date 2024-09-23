"""
Arquivos são uma excelente forma de entrada e saída de dados para o programa. Com eles podemos ler dados de outros programas e mesmo da internet, e podemos salvar dados para serem utilizados posteriormente.

Arquivo é uma área do disco na qual podemos ler e gravar informaçoes. essa área é gerenciada pelo sistema operacional do computador.

PARA ACESSAR UM ARQUIVO PRECISAMOS:
    - abrir o arquivo
    - ler ou gravar informações
    - fechar o arquivo
    a FUNÇÃO QUE FAZ A ABERTURA DO ARQUIVO É A OPEN()
    a FUNÇÃO QUE FAZ O FECHAMENTO DO ARQUIVO É A CLOSE()
    
    a FUNÇÃO QUE FAZ A LEITURA DO ARQUIVO É A READ()
    a FUNÇÃO QUE FAZ A GRAVAÇÃO DO ARQUIVO É A WRITE()
    a FUNÇÃO QUE FAZ A LEITURA DE LINHAS DO ARQUIVO É A READLINES()
    a FUNÇÃO QUE FAZ A GRAVAÇÃO DE LINHAS DO ARQUIVO É A WRITELINES()
    a FUNÇÃO QUE FAZ A LEITURA DE UMA LINHA DO ARQUIVO É A READLINE() #sem o plural
    a FUNÇÃO QUE FAZ A GRAVAÇÃO DE UMA LINHA DO ARQUIVO É A WRITELINE() # sem o plural

a função open() utiliza os parametros nome e modo. 

- nome é o nome do arquivo que queremos abrir
- modo é a forma como queremos abrir o arquivo
    - modo 'r' é para leitura
    - modo 'w' é para escrita
    - modo 'a' é para adição (escrita, mas presenvando o conteúdo do arquivo)
    - modo 'b' é para modo binário
    - modo 't' é para modo texto
    - modo '+' é para leitura e escrita
    - modo 'U' é para modo universal
    - modo 'x' é para criar um arquivo
    - modo 'e' é para abrir um arquivo para edição
    - modo 'c' é para abrir um arquivo para criação
    - modo 'n' é para abrir um arquivo para nulo
    - modo 'd' é para abrir um arquivo para deletar
    - modo 'm' é para abrir um arquivo para mover
    - modo 'p' é para abrir um arquivo para copiar
    - modo 's' é para abrir um arquivo para salvar
    - modo 'l' é para abrir um arquivo para ler    
    
A função open retorna um objeto do tipo arquivo (file). esse é o objeto que utilizamos para ler e gravar informações no arquivo.


"""

#exemplo escrever arquivo numeros.txt com 100 linhas em cada linha um número de 1 a 100

# arquivo é um objeto do tipo file que tem como parametro o nome do arquivo e o modo de abertura
arquivo = open("numeros.txt", 'w')

for linha in range(1, 100):
    arquivo.write(f"{linha}\n")
arquivo.close()

# Quando não fechamos o arquivo, corremos o risco de essa memória auxiliar não ser transferida para o disco e, assim, perdermos as informações que escrevemos no arquivo.

#exemplo: programa para ler o arquivo e imprimir as linhas na tela

arquivo = open("numeros.txt", "r")

# para cada linha do arquivo.leiaaslinhas() e imprima a linha
for linha in arquivo.readlines(): #utilizamos o método readlines() para ler todas as linhas do arquivo
    print(linha)
arquivo.close()

"""
Como o fechamento do arquivo é muito importante, e é muito comum esquecermos de fechar o arquivo, 
o python tem uma forma de garantir que o arquivo será fechado.

Estrutura de controle with permite criarmos um contexto, ou seja, um bloco em que o obejto é valido

"""

# exemplo: de uso do with para abrir e fechar o arquivo

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
        
# for fica dentro do contexto do with, e quando o bloco do with termina, o arquivo é fechado automaticamente