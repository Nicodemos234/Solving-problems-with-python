
arrValues = []
posNum = []

for i in range(10):
    newValue = int(input("insira um valor: "))
    arrValues.append(newValue)

for n in arrValues:
    if n > 0:
       posNum.append(n)

media = sum(arrValues)/len(arrValues)

print("Desses valores " +str(len(posNum))+" são positivos, a média é "+str(media)+", o menor valor é "+str(min(arrValues))+" e o maior é "+str(max(arrValues)))
