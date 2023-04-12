from symtable import *
print("Digite o grau da função")
N = int(input("> "))
if N < 1 or N > 2:
    print("Grau inválido")

if N ==1:
    print("A equação é do primeiro grau")
    a = int(input("> "))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = int(input("> "))
        x = Symbol
        x = -b / a
        a*x+b==0
        if -b % a !=0:
            print("x é igual a",-b,"/",a)
        if -b % a ==0:
            print("x é igual a {}".format(int(x)))

if N ==2:
    print("A equação é do segundo grau")
    a = int(input("> "))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = int(input("> "))
        c = int(input("> "))
        x = Symbol
        delta = b**2 + (-4)*a*c

        if delta >= 0:
            x1 = (-b + (delta**0.5)) / (2*a)
            x2 = (-b - (delta**0.5)) / (2*a) 
            
            if (-b - (delta**0.5)) % (2*a) !=0 and (-b + (delta**0.5)) % (2*a) !=0:
                print("x1 é",x1,"e","x2 é",x2)
            if (-b - (delta**0.5)) % (2*a) ==0 and (-b + (delta**0.5)) % (2*a) !=0:
                print("x1 é",int(x1),"e","x2 é",x2)
            if (-b - (delta**0.5)) % (2*a) !=0 and (-b + (delta**0.5)) % (2*a) ==0:
                print("x1 é",x1,"e","x2 é",int(x2))
            if (-b - (delta**0.5)) % (2*a) ==0 and (-b + (delta**0.5)) % (2*a) ==0:
                print("x1 é",int(x1),"e","x2 é",int(x2))
                
        if delta < 0:
            print("Raiz negativa")
