def generar_triangulo_numeros():
    # Encabezado principal estilizado con diseño de caja
    print("╔" + "═" * 45 + "╗")
    print("║" + " 📐 GENERADOR DE TRIÁNGULO DE NÚMEROS 📐 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir hacer varias pruebas
    while True:
        print("\n" + "─" * 47)
        
        # 1. Bucle para asegurar que el usuario ingrese un entero positivo válido
        while True:
            try:
                entrada = input("🔹 Ingresa un número entero positivo para la base: ").strip()
                numero = int(entrada)
                
                if numero <= 0:
                    print("⚠️  [Error]: El número debe ser mayor a 0. Inténtalo de nuevo.\n")
                else:
                    break
            except ValueError:
                print("⚠️  [Error]: Debes ingresar un número entero válido.\n")
                
        # Cabecera del resultado con estilo dinámico
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Resultado: Triángulo con base de {numero} filas".ljust(46) + "│")
        print("└" + "─" * 45 + "┘\n")
        
        # 2. Bucle externo para controlar cada fila con un pequeño margen estético
        for i in range(1, numero + 1):
            fila = "   ".join(str(j) for j in range(1, i + 1))
            # Imprimimos con un padding izquierdo para que parezca centrado o estructurado
            print(f"    {fila}")
            
        print("\n" + "─" * 47)

        # 3. Preguntar si desea generar otro triángulo
        respuesta = input("🔄 ¿Deseas generar otro triángulo? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo con los patrones! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
generar_triangulo_numeros()