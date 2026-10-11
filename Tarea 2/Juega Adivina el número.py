import random



def juego_adivina_numero():
    numero_secreto = random.randint(1, 100) 
    intentos = 0
    adivinado = False

    print( "¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. Intenta adivinarlo.")


    while not adivinado:
        try:
            intento = int(input("Introduce tu intento: "))
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")


juego_adivina_numero()
