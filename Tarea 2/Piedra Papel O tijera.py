import random

def jugar_piedra_papel_tijera():
    # Diccionario que relaciona el número con la opción de texto
    opciones = {
        "1": "piedra",
        "2": "papel",
        "3": "tijera"
    }
    
    print("=" * 45)
    print(" 🎮 ¡BIENVENIDO A PIEDRA, PAPEL O TIJERA! 🎮 ")
    print("=" * 45)

    # 1. Bucle principal para permitir repetir el juego varias veces
    while True:
        print("\nPor favor, selecciona una opción ingresando su número:")
        print("  [1] Selecciona 1 para piedra 🪨")
        print("  [2] Selecciona 2 para papel 📄")
        print("  [3] Selecciona 3 para tijera ✂️")
        
        # Bucle para asegurar que el usuario elija 1, 2 o 3 válido
        while True:
            eleccion_usuario = input("\nTu elección (1, 2 o 3): ").strip()
            
            if eleccion_usuario in opciones:
                usuario = opciones[eleccion_usuario]
                break
            else:
                print("⚠️ Opción no válida. Por favor, ingresa solo 1, 2 o 3.")
                
        # La computadora elige una opción al azar de los valores del diccionario
        computadora = random.choice(list(opciones.values()))
        
        print("\n-------------------------------------------")
        print(f"👤 Tú elegiste: {usuario.capitalize()}")
        print(f"🤖 La computadora eligió: {computadora.capitalize()}")
        print("-------------------------------------------")
        
        # Lógica para determinar el resultado
        if usuario == computadora:
            print("🤝 ¡Es un empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("🎉 ¡Felicidades, ganaste!")
        else:
            print("💻 La computadora gana esta vez. ¡Sigue intentando!")

        # 2. Preguntar si desea seguir jugando
        respuesta = input("\n¿Quieres seguir jugando? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima!")
            break  # Sale del bucle principal y termina el programa

# Punto de entrada para ejecutar el juego
jugar_piedra_papel_tijera()