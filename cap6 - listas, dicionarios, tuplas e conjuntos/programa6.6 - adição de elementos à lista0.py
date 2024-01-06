#programa6.6 - adição de elementos à lista0.py
l=[]
while True:
    n = int(input("digite um numero, ou 0 para sair: "))
    if n == 0:
        break
    l.append(n)
x=0
while x < len(l):
    print(l[x])
    x+=1
