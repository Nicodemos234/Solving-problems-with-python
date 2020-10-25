
custoFabrica = float(input("insira o custo de fábrica: "))
valDistribuidor = custoFabrica * (28/100)
valImpostos = custoFabrica * (45/100)

valorFinal = custoFabrica+valDistribuidor+valImpostos

print("o valor final do carro será: R$"+str(valorFinal))
