
salario = float(input("insira o salário mensal atual: "))

percencutalReajuste = float(input("indique qual o percentual de reajuste: "))

percencutalReajuste = percencutalReajuste/100

novoSalario = salario + (salario * percencutalReajuste)

print("o novo salário será: R$" + str(novoSalario))



