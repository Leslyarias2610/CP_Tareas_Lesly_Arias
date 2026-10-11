def calculadora_simple():
    # Encabezado principal estilizado
    print("╔" + "═" * 45 + "╗")
    print("║" + " 🧮 CALCULADORA SIMPLE 🧮 ".center(45) + "║")
    print("╚" + "═" * 45 + "╝")
    
    # Bucle principal para permitir realizar varias operaciones
    while True:
        print("\n" + "─" * 47)
        
        # 1. Solicitar y validar el primer número
        while True:
            try:
                num1 = float(input("🔹 Ingresa el primer número: ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
        
        # 2. Solicitar y validar el operador
        operadores_validos = ['+', '-', '*', '/']
        while True:
            operador = input("🔹 Ingresa el operador (+, -, *, /): ").strip()
            if operador in operadores_validos:
                break
            print("⚠️ [Error]: Operador no válido. Usa únicamente +, -, * o /.")
            
        # 3. Solicitar y validar el segundo número
        while True:
            try:
                num2 = float(input("🔹 Ingresa el segundo número: ").strip())
                break
            except ValueError:
                print("⚠️ [Error]: Debes ingresar un valor numérico válido.")
                
        # 4. Realizar la operación correspondiente con control de flujo
        resultado = None
        hubo_error = False
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print("\n⚠️ [Error Matemático]: No es posible dividir entre cero.")
                hubo_error = True
            else:
                resultado = num1 / num2
                
        # 5. Mostrar el resultado de manera elegante si no hubo errores
        if not hubo_error:
            print("\n" + "┌" + "─" * 45 + "┐")
            # Si el resultado es un número entero exacto, lo mostramos sin decimales molestos
            if resultado.is_integer():
                resultado = int(resultado)
            print(f"│ 📊 Resultado: {num1} {operador} {num2} = {resultado}".ljust(46) + "│")
            print("└" + "─" * 45 + "┘")
            
        print("\n" + "─" * 47)
        
        # 6. Preguntar si desea realizar otra operación
        respuesta = input("🔄 ¿Deseas hacer otra operación? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n✨ ¡Excelente trabajo con la calculadora! ¡Hasta pronto! ✨\n")
            break  # Termina el programa

# Punto de entrada para ejecutar el programa
calculadora_simple()