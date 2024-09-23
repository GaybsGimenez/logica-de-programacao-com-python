s = "um, tigre, dois tigres, três tigres"
p = 0 # posição inicial

while (p > -1):
     p = s.find("tigre", p) # procura a próxima ocorrência
     if p >= 0:
         print(f" Posição: {p}")
         p = p + 1
         
         
"""
find() retorna a posição da primeira ocorrência da substring passada como argumento.
rfind() retorna a posição da última ocorrência da substring passada como argumento.

tanto o find() quanto o rfind() suportam duas opções adicionais:
inicio(start) e fim(end), que permitem restringir a busca a uma faixa específica da string


__________________________________________________________________________________________________________________________________________________


método index e rindex, são bem parecidos com os métodos find e rfind, respectivamente. A maior diferença é que, se a substring não for encontrada
o método index() gera uma exceção ValueError, enquanto o método find() retorna -1.
"""

# Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
# 1ª string: AABBEFAATT
# 2ª string: BE
# Resultado: BE encontrado na posição 3 em AABBEFAATT

s1 = "AABBEFAATT"
s2 = "BE"
p = s1.find(s2)
if p == 1:
    print(f"{s2} encontrado na posição {p} em {s1}")
else:
    print(f"{s2} não encontrado em {s1}")
    
# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
# 1ª string: AAACTBF
# 2ª string: CBT
# Resultado: ACTB

s1 = 'AAACTBF'
s2 = 'CBT'
s3 = ''

for caracter in s1:
    if caracter in s2:
        s3.append(caracter)
print(s3)

# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
# 1ª string: Ameixa
# 2ª string: Amor
# Resultado: ei

s1 = 'Ameixa'
s2 = 'Amor'
s3 = ''

for caracter in s1:
    if  caracter not in s2:
        s3.append(caracter)
print(s3)

# Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
# 1ª string: CTA
# 2ª string: ABC

for caracter in s1:
    if caracter in s2:
        s3.append(caracter)
        
# Escreva umprograma que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC

for caracter in s1:
    aparece = s1.count(caracter)
    print(f"{caracter}: {aparece}")
    
# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
# 1ª string: AATTGGAA
# 2ª string: TG

s1 = 'AATTGGAA'
s2 = 'TG'

# converte as strings em conjuntos
s1 = set(s1)
s2 = set(s2)
# subtrai um conjunto do outro
s3 = s1 - s2
print(s3)
# resultado é um conjunto com {'A'}. Para converter o conjunto em string, basta usar o método join().

s3 = ''.join(s3)
print(s3)
# resultado é a string 'A'

# Não foi isso que o exercicio pediu, só queria testar o método join() e o método set(), com string. Resolução exercicio. 

for caracter in s1:
    if caracter not in s2:
        s3.append(caracter)
print(s3)
# resultado é a string 'AA'

# Escreva um programa que leia tres strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira
# 1ª string: AATTCGA
# 2ª string: TG
# 3ª string: AC
# Resultado: AACCCGA

s1 = 'AATTCGA'
s2 = 'TG'
s3 = 'AC'

# para cada caractere da segunda string, usou-se o método range() para gerar uma sequência de números de 0 até o tamanho da string.
for caractere in range(len(s2)):
    # s1 vai receber a substituição do caractere da segunda string pelo caractere da terceira string., metodo replace() é usado para substituir valores.
    s1 = s1.replace(s2[caractere], s3[caractere])
print(s1)
# resultado é a string 'AACCCGA'


