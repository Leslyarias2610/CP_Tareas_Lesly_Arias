def contar_vocales():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🔤 CONTADOR DE VOCALES EN FRASES 🔤 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir analizar varias frases
    while True:
        print("\n" + "─" * 47)
        frase = input("✍️ Ingresa una frase o texto: ").strip()
        
        # Validar que la frase no esté vacía usando continue
        if not frase:
            print("⚠️ [Error]: La frase no puede estar vacía. Inténtalo de nuevo.")
            continue
            
        # Convertimos la frase a minúsculas para unificar criterios
        frase_minuscula = frase.lower()
        
        # Contadores individuales y total
        conteo_total = 0
        detalle_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        # 1. Recorrer cada carácter de la frase usando un bucle for
        for letra in frase_minuscula:
            # 2. Usar estructuras condicionales para identificar vocales (incluyendo acentuadas)
            if letra in 'aá':
                detalle_vocales['a'] += 1
                conteo_total += 1
            elif letra in 'eé':
                detalle_vocales['e'] += 1
                conteo_total += 1
            elif letra in 'ií':
                detalle_vocales['i'] += 1
                conteo_total += 1
            elif letra in 'oó':
                detalle_vocales['o'] += 1
                conteo_total += 1
            elif letra in 'uú':
                detalle_vocales['u'] += 1
                conteo_total += 1

        # 3. Mostrar los resultados de forma ordenada y profesional
        print("\n" + "┌" + "─" * 45 + "┐")
        print(f"│ 📊 Resultados del análisis de texto:".ljust(46) + "│")
        print("└" + "─" * 45 + "┘")
        print(f"✨ Cantidad total de vocales: {conteo_total}")
        
        print("\n📋 Desglose detallado por vocal:")
        for vocal, cantidad in detalle_vocales.items():
            print(f"  • Vocal '{vocal.upper()}': {cantidad} vez/veces")
            
        print("\n" + "─" * 47)
        
        # 4. Preguntar si desea analizar otra frase
        respuesta = input("🔄 ¿Deseas analizar otra frase? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando el procesamiento de texto! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
contar_vocales()