esp="s"
while esp=="s":
    nun = int(input("Digite um número: "))

    if nun > 0:
        if nun % 2 == 0:
            print("Número par e positivo")
        else:
            print("Número ímpar e positivo")

    else:
        if nun % 2 != 0:
            print("Número par e negativo")
        else:
            print("Número ímpar e negativo")

    esp = input("Deseja digitar outro número? : ")

