salmin=float(input("diga quanto estar o salario minimo: "))
while salmin !=0:
    sala=float(input("diga qual salario deseja calcular: "))
    if sala==0:
        print("nao tem salario")
        break

    devisao = sala / salmin
    print(F" voce recebe {devisao} tantos salarios")
