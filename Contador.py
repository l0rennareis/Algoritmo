i=int(input("Digite quantas idades serão informadas: "))
m=0
me=1000
cont=0
while (cont<1):
    a=int(input("Digite sua idade: "))
    if (a>m):
     m=a
     if (a<me):
        me=a
    cont=cont+1
    print("A maior idade é:", m, "e a menor idade é ", me)
