
horaIni = int(input("Digite a hora inicial do jogo: "))
horaFin = int(input("Digite a hora final do jogo: "))

if horaIni < horaFin:
    duracao = horaFin - horaIni
    print("O jogo durou "+str(duracao)+" horas.")
else:
    horaFin = horaFin + 24
    duracao = horaFin - horaIni
    print("O jogo durou "+str(duracao)+" horas.")
