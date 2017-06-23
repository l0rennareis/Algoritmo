x="s"
while x=="s":
 n=input("digite o nome do nadador: ")
 print ("oi"+n)
 i=int(input("digite a idade do nadador:" ))
 if i>=18:
        print("adulto")
 elif i>=14:
        print("juvenil b")
 elif i>=11:
        print("juvenil a")
 elif i>=8:
        print("infantil b")
 elif i>=5:
        print("infantil a")
 x=input ("quer calcular de novo? [s/n]:")
