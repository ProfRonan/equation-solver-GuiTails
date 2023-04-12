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
        x = int
        x = -b / a
        a*x+b==0
        print(x)
        print(a*x+b==0)

if N ==2:
    a = int(input("A equação é do segundo grau"))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = int(input("> "))
        c = int(input("> "))
        x = int
        delta = b**2 + (-4)*a*c

        if delta > 0:
            x1 = (-b - (delta**0.5)) / (2*a) 
            x2 = (-b + (delta**0.5)) / (2*a)
            print("A equação possui duas raízes reais")
            print(x1,x2)
        if delta ==0:
            x3 = (-b + (delta**0.5)) / (2*a)
            print("A equação possui apenas uma raiz real")
            print(x3)
        if delta < 0:
            x1 = (-b - (delta**0.5)) / (2*a) 
            x2 = (-b + (delta**0.5)) / (2*a) 
            print("A equação não possui raízes reais")
