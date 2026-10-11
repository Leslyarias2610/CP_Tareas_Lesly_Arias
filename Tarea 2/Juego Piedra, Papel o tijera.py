import random


import random


def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    while True:
        usuario = (
            input("Elige piedra, papel o tijera (o 'salir' para terminar): ")
            .lower()
            .strip()
        )
        if usuario in opciones or usuario == "salir":
            break
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")

    if usuario == "salir":
        return

    computadora = random.choice(opciones)

    print(f"\nTú elegiste: {usuario.capitalize()}")
    print(f"La computadora eligió: {computadora.capitalize()}\n")

    # AQUÍ ESTABA EL ERROR (Usa '==' en lugar de '--')
    if usuario == computadora:
        print("¡Es un empate!")
    elif (
        (usuario == "piedra" and computadora == "tijera")
        or (usuario == "papel" and computadora == "piedra")
        or (usuario == "tijera" and computadora == "papel")
    ):
        print("¡Ganaste esta ronda!")
    else:
        print("¡Perdiste esta ronda!")


jugar_piedra_papel_tijera()