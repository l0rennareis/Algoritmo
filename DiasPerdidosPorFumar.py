cigarro=int(input("Digite quantos cigarros você fuma por dia: "))
ano=int(input("Digite por quantos anos você já fuma: "))

totalCigarros = (ano * 365)*cigarro
diasPerdidos = (totalCigarros * 10)/24

print ("Você perdeu: %d" %diasPerdidos, "dias" )
