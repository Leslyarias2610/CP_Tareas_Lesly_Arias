def calcular_area_triangulo():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 📐 CÁLCULO DEL ÁREA DE UN TRIÁNGULO 📐 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varios cálculos
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar la base (debe ser mayor a 0)
        while True:
            try:
                base = float(input("🔹 Ingresa la base del triángulo: ").strip())
                if base <= 0:
                    print("⚠️ [Error]: La base debe ser un número mayor a 0.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Solicitar y validar la altura (debe ser mayor a 0)
        while True:
            try:
                altura = float(input("🔹 Ingresa la altura del triángulo: ").strip())
                if altura <= 0:
                    print("⚠️ [Error]: La altura debe ser un número mayor a 0.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
                
        # 3. Calcular el área del triángulo
        area = (base * altura) / 2
        
        # Si el área es un número entero exacto, la manejamos como entero para mayor prolijidad
        if area.is_integer():
            area = int(area)
            if isinstance(base, float) and base.is_integer(): base = int(base)
            if isinstance(altura, float) and altura.is_integer(): altura = int(altura)

        # 4. Mostrar el resultado de manera elegante
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Proceso: ({base} × {altura}) / 2".ljust(46) + "│")
        print(f"│ ✨ Área del triángulo: {area} unidades²".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 5. Preguntar si desea calcular otro triángulo
        respuesta = input("🔄 ¿Deseas calcular otro triángulo? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo con la geometría! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calcular_area_triangulo()