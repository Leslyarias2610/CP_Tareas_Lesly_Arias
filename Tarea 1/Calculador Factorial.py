def calcular_factorial():
    print("=" * 45)
    print(" 📐 CALCULADORA DE FACTORIAL MATEMÁTICO 📐 ")
    print("=" * 45)
    
    # Bucle principal para permitir consultar varios números
    while True:
        # 1. Bucle para asegurar que el usuario ingrese un entero válido no negativo
        while True:
            try:
                entrada = input("\nIngresa un número entero no negativo: ").strip()
                numero = int(entrada)
                
                if numero < 0:
                    print("⚠️ Error: El número no puede ser negativo. Inténtalo de nuevo.")
                else:
                    break
            except ValueError:
                print("⚠️ Error: Debes ingresar un número entero válido.")
                
        # 2. Inicializamos la variable acumuladora en 1
        factorial = 1
        
        # Lista para almacenar los factores y mostrar la explicación detallada
        pasos = []
        
        # 3. Calculamos el factorial usando un bucle for (desde 1 hasta el número)
        for i in range(1, numero + 1):
            factorial *= i  # Acumula la multiplicación
            pasos.append(str(i)) # Guardamos cada número para la explicación

        # 4. Mostramos el resultado y la explicación detallada
        print("\n-------------------------------------------")
        print(f"✨ El factorial de {numero}! es: {factorial}")
        
        # Explicación de por qué se considera ese número factorial
        if numero == 0:
            print("📝 Explicación: Por convención matemática, el factorial de 0 es siempre 1 (0! = 1).")
        else:
            # Unimos los números con un ' x ' para mostrar la operación matemática completa
            operacion_desglosada = " × ".join(pasos)
            print(f"📝 Explicación: Se obtiene multiplicando todos los enteros positivos desde 1 hasta {numero}:")
            print(f"   {numero}! = {operacion_desglosada} = {factorial}")
        print("-------------------------------------------")

        # 5. Preguntar si desea consultar otro número
        respuesta = input("\n¿Deseas consultar otro número? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n👋 ¡Gracias por usar la calculadora factorial! ¡Hasta pronto!")
            break  # Sale del bucle principal y termina el programa

# Punto de entrada para ejecutar el programa
calcular_factorial()