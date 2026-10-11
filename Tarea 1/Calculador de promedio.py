def calcular_promedio_notas():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 📚 CALCULADORA DE PROMEDIO DE NOTAS 📚 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir calcular varios promedios
    while True:
        print("\n" + "─" * 47)
        print("💡 [Criterio]: Aprobado a partir de 60 puntos | Reprobado con menos de 60".center(47))
        print("─" * 47)
        
        # Función auxiliar interna para validar notas entre 0 y 100
        def pedir_nota(nombre_nota):
            while True:
                try:
                    nota = float(input(f"🔹 Ingresa la {nombre_nota} nota (0 - 100): ").strip())
                    if nota < 0 or nota > 100:
                        print("⚠️ [Error]: La nota debe estar en un rango de 0 a 100.")
                    else:
                        return nota
                except ValueError:
                    print("⚠️ [Error]: Debes ingresar un valor numérico válido.")

        # 1. Solicitar y validar las tres notas
        nota1 = pedir_nota("primera")
        nota2 = pedir_nota("segunda")
        nota3 = pedir_nota("tercera")
                
        # 2. Calcular el promedio aritmético
        promedio = (nota1 + nota2 + nota3) / 3
        
        # 3. Determinar el estado académico (Aprobado >= 60 / Reprobado < 60)
        if promedio >= 60:
            estado = "APROBADO (≥ 60 pts)"
            emoji = "🟢"
        else:
            estado = "REPROBADO (< 60 pts)"
            emoji = "🔴"
            
        # Formatear el promedio a dos decimales para mayor limpieza visual
        promedio_str = f"{int(promedio)}" if promedio.is_integer() else f"{promedio:.2f}"

        # 4. Mostrar el resultado de manera elegante en un marco limpio
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Notas ingresadas: [{nota1}, {nota2}, {nota3}]".ljust(46) + "│")
        print(f"│ ✨ Promedio final: {promedio_str}".ljust(46) + "│")
        print(f"│ {emoji} Estado: {estado}".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 5. Preguntar si desea calcular otro promedio
        respuesta = input("🔄 ¿Deseas calcular otro promedio? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo con el módulo académico! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calcular_promedio_notas()