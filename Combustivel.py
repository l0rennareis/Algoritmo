n=int(input("Informe a kilometragem inicial: "))
percorrido=int(input("Informe os kilometros percorridos: "))
litros=int(input("Informe a quantidade de combustivel necessária para completar o tanque: "))

km=percorrido-n
consumo=km/litros

print("Seu consumo médio foi: ",consumo)
