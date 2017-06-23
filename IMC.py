sexo= input("Digite seu sexo: ")
n= input("Digite seu nome: ")
p= float(input("Digite peso: "))
a= float(input("Digite altura: "))
imc= (p)/(a*a)
print(imc)
if sexo==("masculino"):

        if imc<20.7:
            print("abaixo do peso")
        elif imc>=20.7:
            print("Peso ideal")
        elif imc>26.4:
            print("Acima do peso")
        elif imc>27.8:
            print("Acima do peso ideal")

if sexo==("feminino"):

        if imc<19.1:
            print("abaixo do peso")
        elif imc>=19.1:
            print("Peso ideal")
        elif imc>25.8:
            print("Acima do peso")
        elif imc>27.3:
            print("Acima do peso ideal")
        x=input("Quer ver de outra pessoa? [s/n]:")
