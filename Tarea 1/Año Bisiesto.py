def verificar_anio_bisiesto():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 📅 DETECTOR DE AÑO BISIESTO 📅 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir analizar varios años
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar que sea un año entero positivo
        while True:
            try:
                anio = int(input("🔹 Ingresa un año (ej. 2024): ").strip())
                if anio <= 0:
                    print("⚠️ [Error]: Por favor ingresa un año válido mayor a 0.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un número entero válido (sin decimales).")
        
        # 2. Aplicar la lógica del año bisiesto
        # Es divisible por 4, y (no es divisible por 100 o es divisible por 400)
        es_bisiesto = (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)
        
        # 3. Definir mensajes y emojis según el resultado
        if es_bisiesto:
            resultado = "ES UN AÑO BISIESTO (366 días)"
            emoji = "🟢"
        else:
            resultado = "NO ES UN AÑO BISIESTO (365 días)"
            emoji = "🔴"
            
        # 4. Mostrar el resultado de manera elegante
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Análisis matemático para el año {anio}".ljust(46) + "│")
        print(f"│ {emoji} {resultado}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 5. Preguntar si desea verificar otro año
        respuesta = input("🔄 ¿Deseas verificar otro año? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando la lógica temporal! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
verificar_anio_bisiesto()