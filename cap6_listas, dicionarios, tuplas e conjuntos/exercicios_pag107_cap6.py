#6.4 - O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?

# Se não verificarmos que a lista está vazia antes de charmos pop(),
# o programa pára com uma mensagem de erro, informando que tentamos retirar um elemento de uma lista vazia.
# A verificação é necessária para controlar este erro e assegurar o bom funcionamento do programa.

#6.5 Altere o programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido por vez.
#Altere-o de forma a considerar operações com uma string.

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('digite F para adc um cliente ao final da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operacao = input('Operacao que deseja realizar (F, A, ou S): ')
    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia! Ninguém para atender! ')
    elif operacao == 'F':
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else: 
        print('Operacao inválida! Digite apenas F, A ou S!')