# Juego de Piedra Papel o Tijeras
# Autor: David Salazar Rodero
# Github: https://github.com/mrgold92
import random

jugadas = ["Piedra", "Papel", "Tijeras"]


def jugadaPc() -> int:
    return random.randint(0, len(jugadas) - 1)


def menu():
    print("========================================")
    print('0 -> Piedra 1 -> Papel 2 -> Tijeras')
    print("========================================")


def juego(jugada, jugadapc):

    if jugada == jugadapc:
        result = 3
    elif (jugada == 0 and jugadapc == 2):
        result = 1
    elif jugada == 1 and jugadapc == 0:
        result = 1
    elif jugada == 2 and jugadapc == 1:
        result = 1
    else:
        result = 2

    return result


aciertos = 0
print("Elige jugada:")

for i in range(1, 4):

    menu()
    jugada = int(input()) % 3
    jugadapc = jugadaPc()

    result = juego(jugada, jugadapc)

    print(f"·->Tú: {jugadas[jugada]} ·->PC: {jugadas[jugadapc]}")

    if result == 1:
        print("|=====Ganas=======|")
        aciertos += 1
    elif result == 2:
        print("|=====Pierdes=======|")
    else:
        print("|=====Empate=======|")

    print("")

    if i == 3:
        if aciertos >= 2:
            print("Has ganado el juego.")

        print("|/////////////////////////////////|")
        print(f"| Puntuación total: {aciertos:<14}|")
        print("|/////////////////////////////////|")
