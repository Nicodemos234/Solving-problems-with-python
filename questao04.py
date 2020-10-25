
renda = float(input("insira sua renda: "))

if (renda > 2000 and renda <= 3000):
    imposto = (renda - 2000) * (8/100)
    print("O imposto de renda será: R$"+ str(imposto))
elif  (renda > 3000 and renda <= 4500):
    imposto = (renda - 2000) * (18/100)
    print("O imposto de renda será: R$"+ str(imposto))
elif  (renda > 4500):
    imposto = (renda - 2000) * (28/100)
    print("O imposto de renda será: R$"+ str(imposto))
else:
    print("Isento de imposto.")





