print("Digite o grau da função")
N = float(input("> "))
if N !=1 and N !=2:
    print("Grau inválido")

if N ==1:
    print("A equação é do primeiro grau")
    a = float(input("> "))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = float(input("> "))
        x = float
        x = b/a
        print("{:.2f}".format(x))
    
            
if N ==2:
    print("A equação é do segundo grau")
    a = float(input("> "))
    if a ==0:
        print("Valor de a inválido")
    if a !=0:
        b = float(input("> "))
        c = float(input("> "))
        x = float
        delta = b**2 + (-4)*a*c

        if delta > 0:
            x1 = (-b - (delta**0.5)) / (2*a) 
            x2 = (-b + (delta**0.5)) / (2*a)
            print("A equação possui duas raízes reais")
            print("{:.2f}".format(x1),"{:.2f}".format(x2))
        if delta ==0:
            x3 = 0.00
            print("A equação possui uma raiz real")
            print("{:.2f}".format(x3))
        if delta < 0:
            print("A equação não possui raízes reais")
