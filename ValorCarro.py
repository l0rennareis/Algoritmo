valor_do_carro = int(input("Qual o custo de fabrica? "))
taxa_do_distribuidor = (valor_do_carro*28)/100
taxa_de_impostos = (valor_do_carro*45)/100
valor_do_carro=valor_do_carro+taxa_do_distribuidor+taxa_de_impostos
print("o valor do carro é %d"%(valor_do_carro))
