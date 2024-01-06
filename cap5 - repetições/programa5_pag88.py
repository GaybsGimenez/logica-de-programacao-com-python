#programa5_pag88

pontos = 0
questao = 1
while questao <=3:
    resposta = input(f"resposta da questão {questao}: ")
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = ponto + 1
    questao = questao + 1
print(f"O aluno fez {pontos} ponto(s)")

#ex5.10 Modifique o programa anterior para que aceite repostas maiusculas e minusculas em todas as questões:
pontos = 0
questao = 1
while questao <=3:
    resposta = input(f"resposta da questão {questao}: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = ponto + 1
    questao = questao + 1
print(f"O aluno fez {pontos} ponto(s)")
