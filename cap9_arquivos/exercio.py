
# escreva um progrma que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo.
# caso o arquivo não exista, imprima uma mensagem de erro.

'''
Quando você executa um programa Python a partir da linha de comando, você pode passar argumentos para esse programa. 
No caso do programa a seguir, o argumento que queremos passar é o nome do arquivo que queremos imprimir.

Por exemplo, se você tem um arquivo chamado texto.txt e deseja imprimir o conteúdo desse arquivo, 
você irá executar o programa Python da seguinte forma:

1. Abra o terminal ou prompt de comando
2. Navegue até o diretório onde o arquivo Python (programa.py) e o arquivo que você deseja imprimir (texto.txt) estão localizados.
3. Execute o seguinte comando:


>> python programa.py texto.txt <<


python: é o comando para executar o interpretador Python.
programa.py: é o nome do arquivo Python que você quer executar.
texto.txt: é o argumento que você está passando para o programa. Este é o nome do arquivo que você deseja imprimir.
O programa Python então receberá esse argumento (texto.txt neste caso), abrirá o arquivo com esse nome e imprimirá 
o conteúdo desse arquivo. Se o arquivo não estiver no mesmo diretório do programa Python, 
você precisará especificar o caminho completo para o arquivo.

'''
import sys

if len(sys.argv) != 2:
    print("Uso: python programa.py <nome_do_arquivo>")
    sys.exit(1)

nome_arquivo = sys.argv[1]

try:
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha, end='')
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



# Após navegar até o diretório correto, você pode executar o programa Python da seguinte maneira:

# >>> python exercicio.py texto.txt