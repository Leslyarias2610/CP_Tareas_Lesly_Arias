import string

def validar_contrasena():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🔒 VALIDADOR DE CONTRASEÑAS SEGURAS 🔒 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir validar varias contraseñas
    while True:
        print("\n" + "─" * 47)
        print("📋 Criterios de seguridad requeridos:")
        print("  • Mínimo 8 caracteres")
        print("  • Al menos una letra mayúscula")
        print("  • Al menos una letra minúscula")
        print("  • Al menos un número")
        print("  • Al menos un carácter especial (ej. @, #, $, !, etc.)")
        print("─" * 47)
        
        # Solicitamos la contraseña al usuario
        password = input("\n🔑 Ingresa la contraseña a evaluar: ").strip()
        
        # Lista para acumular los criterios que no se cumplan
        errores = []
        
        # 1. Validar longitud
        if len(password) < 8:
            errores.append("❌ Debe tener al menos 8 caracteres.")
            
        # 2. Validar letra mayúscula
        if not any(c.isupper() for c in password):
            errores.append("❌ Debe contener al menos una letra mayúscula.")
            
        # 3. Validar letra minúscula
        if not any(c.islower() for c in password):
            errores.append("❌ Debe contener al menos una letra minúscula.")
            
        # 4. Validar número
        if not any(c.isdigit() for c in password):
            errores.append("❌ Debe contener al menos un número.")
            
        # 5. Validar carácter especial
        if not any(c in string.punctuation for c in password):
            errores.append("❌ Debe contener al menos un carácter especial (ej. @, #, $, !, etc.).")
            
        # Mostrar el resultado de la validación
        print("\n" + "┌" + "─" * 45 + "┐")
        if errores:
            print(f"│ ⚠️  Resultado: Contraseña NO segura".ljust(46) + "│")
            print("└" + "─" * 45 + "┘")
            print("\nPor favor, corrige los siguientes aspectos:")
            for error in errores:
                print(f"  {error}")
        else:
            print(f"│ ✨ Resultado: ¡Contraseña Segura y Válida!".ljust(46) + "│")
            print("└" + "─" * 45 + "┘")
            print("\n🎉 ¡Felicidades! Tu contraseña cumple con todos los estándares de seguridad.")
            
        print("\n" + "─" * 47)
        
        # Preguntar si desea validar otra contraseña
        respuesta = input("🔄 ¿Deseas evaluar otra contraseña? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo dominando la validación de datos! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
validar_contrasena()