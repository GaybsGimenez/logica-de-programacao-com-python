#programa tabuada_pag93_cap5
tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1

#mesmo problema mas sem usar a repetiçao aninhada

tabuada = 1
numero = 1
while tabuada <= 10:
    print(f"{tabuada} x {numero} = {tabuada * numero}")
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1
        
    
