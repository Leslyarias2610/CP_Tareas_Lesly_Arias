def calcular_factorial():
    print("---Calculadora de Factorial---")
    try:
        numero = int(input("Ingrese un número entero no negativo: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return


    if numero < 0:

        print("Error: El número debe ser no negativo.")
    elif numero == 0:
        print("El factorial de 0!s 1.")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es {factorial}.")


calcular_factorial()