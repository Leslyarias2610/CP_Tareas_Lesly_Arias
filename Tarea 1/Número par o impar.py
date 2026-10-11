def verificar_par_impar():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🔢 DETERMINADOR DE NÚMERO PAR O IMPAR 🔢 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir analizar varios números
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar que sea un número entero
        while True:
            try:
                numero = int(input("🔹 Ingresa un número entero: ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un número entero válido (sin decimales).")
        
        # 2. Determinar si es par o impar usando el operador módulo (%)
        if numero % 2 == 0:
            resultado = "PAR"
            emoji = "🟩"
        else:
            resultado = "IMPAR"
            emoji = "🟦"
            
        # 3. Mostrar el resultado de manera elegante
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Análisis: {numero} % 2 = {numero % 2}".ljust(46) + "│")
        print(f"│ {emoji} El número {numero} es: {resultado}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 4. Preguntar si desea analizar otro número
        respuesta = input("🔄 ¿Deseas verificar otro número? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando el operador módulo! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
verificar_par_impar()