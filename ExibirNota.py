n=input("digite seu nome: ")
print("Ola "+n)
n1=float(input("Digite N1: "))
n2=float(input("Digite N2: "))
n3=float(input("Digite N3: "))
n4=float(input("Digite N4: "))
m=(n1+n2+n3+n4)/4
print("ola %s vou exibir sua nota: "%n)
print(m)
print("ola %s sua nota foi %6.2f"%(n, m))
if m>=9:
    print("otimo")
else:
    if m>=7:
        print("bom")
    else:
        if m>=6:
            print("suficiente")
        else:
            print("insuficiente")

