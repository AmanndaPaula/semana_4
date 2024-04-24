num = int(input("De qual número será a tabuada: "))
inicio = int(input("Por qual número vai começar: "))
fim = int(input("Com qual número você quer terminar: "))


if fim < inicio:
    print("Erro: O número final deve ser maior ou igual ao número inicial.")
else:
    print(f"Tabuada do {num} de {inicio} até {fim}:")

    for i in range(inicio, fim + 1):
        print(f"{num} x {i} = {num*i}")