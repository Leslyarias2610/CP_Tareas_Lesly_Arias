def determinar_mayor():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " ⚖️ COMPARADOR: ¿CUÁL ES EL MAYOR? ⚖️ ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varias comparaciones
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar el primer número
        while True:
            try:
                num1 = float(input("🔹 Ingresa el primer número: ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Solicitar y validar el segundo número
        while True:
            try:
                num2 = float(input("🔹 Ingresa el segundo número: ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
                
        # Ajustar enteros para evitar decimales molestos en la visualización
        num1_val = int(num1) if num1.is_integer() else num1
        num2_val = int(num2) if num2.is_integer() else num2
        
        # 3. Determinar cuál es mayor o si son iguales
        if num1 > num2:
            mensaje = f"✨ El número mayor es: {num1_val}"
            emoji = "🥇"
        elif num2 > num1:
            mensaje = f"✨ El número mayor es: {num2_val}"
            emoji = "🥈"
        else:
            mensaje = f"✨ ¡Ambos números son iguales ({num1_val})!"
            emoji = "⚖️"
            
        # 4. Mostrar el resultado de manera elegante
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Comparación: {num1_val} vs {num2_val}".ljust(46) + "│")
        print(f"│ {emoji} {mensaje}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 5. Preguntar si desea realizar otra comparación
        respuesta = input("🔄 ¿Deseas comparar otros números? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo comparando números! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
determinar_mayor()