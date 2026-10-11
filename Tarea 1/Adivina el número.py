import random

def adivina_el_numero():
    # 1. Generamos un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He seleccionado un número entre 1 y 100. ¿Puedes adivinar cuál es?\n")
    
    # 2. Iniciamos un bucle infinito que solo se detendrá cuando el usuario acierte
    while True:
        try:
            # Pedimos el número al usuario y lo convertimos a entero
            intento = int(input("Escribe tu número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue  # Vuelve al inicio del bucle si escriben letras
        
        # 3. Evaluamos las pistas comparando los valores
        if intento < numero_secreto:
            print("Demasiado bajo. El número secreto es mayor 📈.\n")
        elif intento > numero_secreto:
            print("Demasiado alto. El número secreto es menor 📉.\n")
        else:
            print(f"🎉 ¡Felicidades! Adivinaste el número correcto ({numero_secreto}).")
            break  # Rompemos el ciclo porque el juego terminó

# Ejecutamos la función principal
adivina_el_numero()