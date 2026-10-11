def convertir_temperatura():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🌡️ CONVERSOR DE TEMPERATURA (°C a °F) 🌡️ ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varias conversiones
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar la temperatura en Celsius
        while True:
            try:
                celsius = float(input("🔹 Ingresa la temperatura en grados Celsius (°C): ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Realizar la conversión a Fahrenheit
        fahrenheit = (celsius * 9 / 5) + 32
        
        # Si los valores son enteros exactos, los ajustamos para mostrarlos más limpios
        if celsius.is_integer():
            celsius_mostrar = int(celsius)
        else:
            celsius_mostrar = celsius
            
        if fahrenheit.is_integer():
            fahrenheit_mostrar = int(fahrenheit)
        else:
            # Mostramos hasta 2 decimales si los tiene para mayor precisión
            fahrenheit_mostrar = round(fahrenheit, 2)

        # 3. Mostrar el resultado de manera elegante
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Fórmula: ({celsius_mostrar} × 9/5) + 32".ljust(46) + "│")
        print(f"│ ✨ Resultado: {celsius_mostrar} °C = {fahrenheit_mostrar} °F".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 4. Preguntar si desea realizar otra conversión
        respuesta = input("🔄 ¿Deseas convertir otra temperatura? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando la conversión de unidades! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
convertir_temperatura()