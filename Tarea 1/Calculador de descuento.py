def calcular_descuento():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🏷️ CALCULADORA DE DESCUENTO COMERCIAL 🏷️ ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varios cálculos
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar el precio del producto (mayor a 0)
        while True:
            try:
                precio = float(input("🔹 Ingresa el precio original del producto: ").strip())
                if precio <= 0:
                    print("⚠️ [Error]: El precio debe ser un número mayor a 0.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Solicitar y validar el porcentaje de descuento (entre 0 y 100)
        while True:
            try:
                porcentaje = float(input("🔹 Ingresa el porcentaje de descuento (ej. 15 para 15%): ").strip())
                if porcentaje < 0 or porcentaje > 100:
                    print("⚠️ [Error]: El porcentaje de descuento debe estar entre 0 y 100.")
                else:
                    break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
                
        # 3. Realizar los cálculos comerciales
        monto_descuento = precio * (porcentaje / 100)
        precio_final = precio - monto_descuento
        
        # Formatear de manera limpia los valores según sean enteros o decimales
        precio_str = f"{int(precio):,}" if precio.is_integer() else f"{precio:,.2f}"
        porc_str = f"{int(porcentaje)}" if porcentaje.is_integer() else f"{porcentaje:.2f}"
        ahorro_str = f"{int(monto_descuento):,}" if monto_descuento.is_integer() else f"{monto_descuento:,.2f}"
        final_str = f"{int(precio_final):,}" if precio_final.is_integer() else f"{precio_final:,.2f}"

        # 4. Mostrar el resultado de manera elegante en un marco limpio
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Precio original: ${precio_str}".ljust(46) + "│")
        print(f"│ 📉 Descuento aplicado: {porc_str}% (-${ahorro_str})".ljust(46) + "│")
        print(f"│ ✨ Precio final a pagar: ${final_str}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 5. Preguntar si desea calcular otro descuento
        respuesta = input("🔄 ¿Deseas calcular otro descuento? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando las operaciones financieras! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calcular_descuento()