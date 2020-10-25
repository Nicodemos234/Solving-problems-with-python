
qtdMercadorias = int(input("Insira o total de mercadorias: "))
aux = 1
somaMercadoria = 0

while aux <= qtdMercadorias:
    somaMercadoria = somaMercadoria + float(input("insira o valor da "+ str(aux)+"ª mercadoria: "))
    aux = aux+1

mediaValMerc = somaMercadoria/qtdMercadorias
print("o valor total em estoque é de R$"+str(somaMercadoria)+" e a média de valor das mercadorias é igual a R$"+str(mediaValMerc))
