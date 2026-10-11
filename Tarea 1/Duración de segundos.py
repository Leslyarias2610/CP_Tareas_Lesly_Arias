def calcular_duracion_segundos():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " ⏱️ CONVERSOR DE TIEMPO A SEGUNDOS ⏱️ ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varias conversiones
    while True:
        print("\n" + "─" * 47)
        
        # Función auxiliar interna para validar enteros no negativos
        def pedir_tiempo(unidad):
            while True:
                try:
                    valor = int(input(f"🔹 Ingresa la cantidad de {unidad}: ").strip())
                    if valor < 0:
                        print(f"⚠️ [Error]: Las {unidad} no pueden ser negativas.")
                    else:
                        return valor
                except ValueError:
                    print("⚠️ [Error]: Debes ingresar un número entero válido.")

        # 1. Solicitar y validar horas, minutos y segundos
        horas = pedir_tiempo("horas")
        minutos = pedir_tiempo("minutos")
        segundos = pedir_tiempo("segundos")
                
        # 2. Calcular el total en segundos
        total_segundos = (horas * 3600) + (minutos * 60) + segundos
        
        # Formatear el total con separadores de miles para mayor legibilidad
        total_formateado = f"{total_segundos:,}".replace(",", ".")

        # 3. Mostrar el resultado de manera elegante en un marco limpio
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 🕒 Tiempo ingresado: {horas}h : {minutos}m : {segundos}s".ljust(46) + "│")
        print(f"│ ✨ Duración total: {total_formateado} segundos".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 4. Preguntar si desea realizar otra conversión
        respuesta = input("🔄 ¿Deseas convertir otro tiempo? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando la conversión temporal! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calcular_duracion_segundos()