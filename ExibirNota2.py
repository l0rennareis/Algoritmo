x=1
while x<4:
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
   sit="otimo"
 elif m>=7:
   sit="bom"
 elif m>=6:
   sit="suficiente"
 else:
   sit="insuficiente"
   print(sit)
   print("ola %s sua nota foi %2.2f e ficou %s"%(n, m, sit))
   x=x+1
