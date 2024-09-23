#método fila.pop() - programa6.7 - simulação de uma fila
#fila: a inclusão é sempre realizada no fim e as remoções no começo (primeiro que entra, primeiro que sai) - first in first out

ultimo = 10
fila = list(range( 1, ultimo + 1))
while True:
    print(f'\nexistem {len(fila)} clientes na fila')
    print(f'fila atual: {fila}')
    print('digite F para adc um cliente ao fim da fila, ')
    print('ou A para realizar o atendimento. S para sair. ')
    operacao = input('operacao que deseja realizar (F, A ou S): ')
    if operacao == 'A':
        atendido = fila.pop(0)
        print(f'cliente{atendido} atendido')
    else:
        print('fila vazia. ninguém para atender')
elif operacao == 'F':
    ultimo += 1
    fila.append(ultimo)
elif operacao == 'S':
    break
else:
    print('operacao inválida!digite apenas F, A ou S!')
        
        
