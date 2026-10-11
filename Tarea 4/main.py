# main.py
import unicodedata
from metro import GRAFO_METRO, LINEAS_ESTACION, obtener_estaciones_de_linea, obtener_lineas_de_estacion
from planificador import calcular_ruta_optima


def normalizar_texto(texto: str) -> str:
    """
    Elimina tildes y convierte el texto a minúsculas para 
    facilitar las comparaciones flexibles con el usuario.
    """
    texto = texto.strip().lower()
    # Eliminar signos de acentuación
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


def buscar_estacion_oficial(entrada_usuario: str) -> str:
    """
    Busca la coincidencia exacta de la estación en la base de datos,
    ignorando diferencias de mayúsculas o tildes.
    Devuelve el nombre oficial (ej. 'Pérez Bonalde') o None si no existe.
    """
    entrada_norm = normalizar_texto(entrada_usuario)
    for estacion_oficial in GRAFO_METRO.keys():
        if normalizar_texto(estacion_oficial) == entrada_norm:
            return estacion_oficial
    return None


def menu_consultar_linea():
    """Opción 1: Consultar qué estaciones pertenecen a una línea."""
    print("\n--- CONSULTAR ESTACIONES POR LÍNEA ---")
    linea = input("Ingrese la línea (ej. L1, L3, L4, L5): ").strip().upper()
    estaciones = obtener_estaciones_de_linea(linea)

    if estaciones:
        print(f"\nEstaciones pertenecientes a la {linea}:")
        for i, est in enumerate(estaciones, 1):
            print(f"  {i}. {est}")
    else:
        print(f"\n[!] La línea '{linea}' no existe o no tiene estaciones registradas.")

    print("\n" + "─" * 47)
    input("🔹 Presiona [Enter] para continuar... ")


def menu_consultar_estacion():
    """Opción 2: Consultar las líneas que pasan por una estación."""
    print("\n--- CONSULTAR LÍNEAS DE UNA ESTACIÓN ---")
    entrada = input("Ingrese el nombre de la estación: ")
    estacion_oficial = buscar_estacion_oficial(entrada)

    if estacion_oficial:
        lineas = obtener_lineas_de_estacion(estacion_oficial)
        print(f"\nLa estación '{estacion_oficial}' pertenece a: {', '.join(lineas)}")
    else:
        print(f"\n[!] La estación '{entrada}' no fue encontrada en el sistema.")

    print("\n" + "─" * 47)
    input("🔹 Presiona [Enter] para continuar... ")


def menu_planificar_ruta():
    """Opción 3: Planificar la ruta óptima entre origen y destino."""
    print("\n--- PLANIFICADOR DE RUTAS ---")
    origen_raw = input("Ingrese estación de ORIGEN: ")
    destino_raw = input("Ingrese estación de DESTINO: ")

    origen = buscar_estacion_oficial(origen_raw)
    destino = buscar_estacion_oficial(destino_raw)

    if not origen:
        print(f"\n[!] Error: La estación de origen '{origen_raw}' no existe.")
        print("\n" + "─" * 47)
        input("🔹 Presiona [Enter] para continuar... ")
        return
    if not destino:
        print(f"\n[!] Error: La estación de destino '{destino_raw}' no existe.")
        print("\n" + "─" * 47)
        input("🔹 Presiona [Enter] para continuar... ")
        return

    # Cálculo mediante el planificador
    resultado = calcular_ruta_optima(origen, destino)

    if "error" in resultado:
        print(f"\n[!] {resultado['error']}")
        print("\n" + "─" * 47)
        input("🔹 Presiona [Enter] para continuar... ")
        return

    # Presentación de resultados
    print("\n==============================================")
    print("               RESUMEN DEL ITINERARIO         ")
    print("==============================================")
    print(f" Origen:  {origen}")
    print(f" Destino: {destino}")
    print(f" Tiempo estimado: {resultado['tiempo_total']} minutos")
    print(f" Total estaciones: {resultado['total_estaciones']}")
    print("----------------------------------------------")
    print("Ruta a recorrer:")
    print(" -> ".join(resultado['ruta']))
    print("----------------------------------------------")

    # Notificación de transbordos
    if resultado['transbordos']:
        print(" TRANSBORDOS REQUERIDOS:")
        for t in resultado['transbordos']:
            print(f"  • En '{t['estacion']}': Cambiar de {t['linea_salida']} a {t['linea_llegada']}")
    else:
        print(" Directo: No requiere cambio de línea.")
    print("==============================================")
    
    print("\n" + "─" * 47)
    input("🔹 Presiona [Enter] para continuar... ")


def main():
    """Bucle principal de la interfaz de línea de comandos (CLI)."""
    while True:
        print("\n==============================================")
        print("   SISTEMA DE METRO DE CARACAS - MENÚ        ")
        print("==============================================")
        print("1. Consultar estaciones de una línea")
        print("2. Consultar líneas de una estación")
        print("3. Planificar ruta (Origen -> Destino)")
        print("4. Salir")
        print("==============================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            menu_consultar_linea()
        elif opcion == "2":
            menu_consultar_estacion()
        elif opcion == "3":
            menu_planificar_ruta()
        elif opcion == "4":
            print("\n¡Gracias por utilizar el sistema del Metro de Caracas! Buen viaje.\n")
            break
        else:
            print("\n[!] Opción inválida. Intente de nuevo.")
            print("\n" + "─" * 47)
            input("🔹 Presiona [Enter] para continuar... ")


if __name__ == "__main__":
    main()