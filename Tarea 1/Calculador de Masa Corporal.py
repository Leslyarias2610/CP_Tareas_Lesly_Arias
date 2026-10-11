def calcular_imc():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " ⚖️ CALCULADORA DE ÍNDICE DE MASA CORPORAL ⚖️ ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varios cálculos
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar el peso (mayor a 0)
        while True:
            try:
                peso = float(input("🔹 Ingresa tu peso en kg (ej. 70.5): ").strip())
                if peso <= 0:
                    print("⚠️ [Error]: El peso debe ser un valor mayor a 0.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Solicitar y validar la altura (mayor a 0 y un rango humano lógico)
        while True:
            try:
                altura = float(input("🔹 Ingresa tu altura en metros (ej. 1.75): ").strip())
                if altura <= 0 or altura > 3.0:
                    print("⚠️ [Error]: Por favor ingresa una altura válida en metros (ej. 1.75).")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
                
        # 3. Calcular el IMC utilizando la fórmula
        imc = peso / (altura ** 2)
        
        # 4. Determinar la categoría según los rangos estándar
        if imc < 18.5:
            categoria = "Bajo peso"
            emoji = "🔵"
        elif 18.5 <= imc < 25:
            categoria = "Peso normal (Saludable)"
            emoji = "🟢"
        elif 25 <= imc < 30:
            categoria = "Sobrepeso"
            emoji = "🟡"
        else:
            categoria = "Obesidad"
            emoji = "🔴"
            
        # 5. Mostrar el resultado de manera elegante en un marco limpio
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Datos: {peso} kg | Altura: {altura} m".ljust(46) + "│")
        print(f"│ ✨ Tu IMC calculado es: {imc:.2f}".ljust(46) + "│")
        print(f"│ {emoji} Categoría: {categoria}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 6. Preguntar si desea realizar otro cálculo
        respuesta = input("🔄 ¿Deseas calcular otro IMC? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo con este módulo de salud! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calcular_imc()