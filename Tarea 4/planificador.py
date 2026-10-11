# planificador.py
import heapq
from metro import GRAFO_METRO, LINEAS_ESTACION, existe_estacion


def obtener_linea_comun(estacion1: str, estacion2: str) -> str:
    """
    Encuentra la línea que comparten dos estaciones contiguas.
    Devuelve el nombre de la línea (ej. 'L1') o None si no coinciden.
    """
    lineas_e1 = set(LINEAS_ESTACION.get(estacion1, []))
    lineas_e2 = set(LINEAS_ESTACION.get(estacion2, []))
    coincidencias = lineas_e1.intersection(lineas_e2)

    if coincidencias:
        return list(coincidencias)[0]
    return None


def identificar_transbordos(ruta: list) -> list:
    """
    Analiza la secuencia de la ruta y detecta en qué estaciones
    ocurre un cambio de línea o transferencia peatonal.
    """
    if len(ruta) < 2:
        return []

    transbordos = []
    linea_actual = obtener_linea_comun(ruta[0], ruta[1])

    for i in range(len(ruta) - 1):
        estacion_actual = ruta[i]
        estacion_siguiente = ruta[i + 1]
        linea_siguiente = obtener_linea_comun(estacion_actual, estacion_siguiente)

        # Caso 1: Pasillo de transferencia entre estaciones conectadas (ej. Plaza Venezuela -> Zona Rental)
        if linea_siguiente is None:
            lineas_origen = LINEAS_ESTACION.get(estacion_actual, [])
            lineas_destino = LINEAS_ESTACION.get(estacion_siguiente, [])
            transbordos.append({
                "estacion": f"{estacion_actual} ➔ {estacion_siguiente}",
                "linea_salida": "/".join(lineas_origen),
                "linea_llegada": "/".join(lineas_destino)
            })
            continue

        # Caso 2: Cambio de línea en un nodo de transferencia (ej. Capuchinos de L4 a L2)
        if linea_actual and linea_siguiente != linea_actual:
            transbordos.append({
                "estacion": estacion_actual,
                "linea_salida": linea_actual,
                "linea_llegada": linea_siguiente
            })

        linea_actual = linea_siguiente

    return transbordos


def calcular_ruta_optima(origen: str, destino: str) -> dict:
    """
    Calcula la ruta más rápida entre origen y destino usando Dijkstra.
    Devuelve un diccionario con el tiempo total, las estaciones y los transbordos.
    """
    # 1. Validaciones
    if not existe_estacion(origen) or not existe_estacion(destino):
        return {"error": "Una o ambas estaciones no existen en el sistema."}

    if origen == destino:
        return {
            "tiempo_total": 0,
            "total_estaciones": 1,
            "ruta": [origen],
            "transbordos": []
        }

    # 2. Cola de prioridad (Min-Heap): (tiempo_acumulado, estacion_actual, ruta_recorrida)
    cola_prioridad = [(0, origen, [origen])]
    tiempos_minimos = {origen: 0}

    while cola_prioridad:
        tiempo_actual, nodo_actual, ruta_actual = heapq.heappop(cola_prioridad)

        # Si alcanzamos el destino
        if nodo_actual == destino:
            transbordos = identificar_transbordos(ruta_actual)
            return {
                "tiempo_total": tiempo_actual,
                "total_estaciones": len(ruta_actual),
                "ruta": ruta_actual,
                "transbordos": transbordos
            }

        if tiempo_actual > tiempos_minimos.get(nodo_actual, float('inf')):
            continue

        # Explorar nodos vecinos
        for vecino, tiempo_tramo in GRAFO_METRO.get(nodo_actual, []):
            nuevo_tiempo = tiempo_actual + tiempo_tramo

            if nuevo_tiempo < tiempos_minimos.get(vecino, float('inf')):
                tiempos_minimos[vecino] = nuevo_tiempo
                heapq.heappush(
                    cola_prioridad,
                    (nuevo_tiempo, vecino, ruta_actual + [vecino])
                )

    return {"error": "No existe una ruta disponible entre las estaciones seleccionadas."}


# Prueba rápida de funcionamiento
if __name__ == "__main__":
    # Prueba del caso Zona Rental -> Ruiz Pineda
    resultado = calcular_ruta_optima("Zona Rental", "Ruiz Pineda")
    print("--- PRUEBA DE RUTA (Zona Rental -> Ruiz Pineda) ---")
    print(f"Ruta: {' -> '.join(resultado['ruta'])}")
    print(f"Tiempo total: {resultado['tiempo_total']} minutos")
    print(f"Total estaciones: {resultado['total_estaciones']}")
    print(f"Transbordos: {resultado['transbordos']}")