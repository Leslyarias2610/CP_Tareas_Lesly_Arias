# metro.py

# Diccionario de líneas por estación
LINEAS_ESTACION = {
    # Línea 1
    "Propatria": ["L1"],
    "Pérez Bonalde": ["L1"],
    "Plaza Sucre": ["L1"],
    "Gato Negro": ["L1"],
    "Agua Salud": ["L1"],
    "Caño Amarillo": ["L1"],
    "Capitolio": ["L1"],
    "La Hoyada": ["L1"],
    "Parque Carabobo": ["L1"],
    "Bellas Artes": ["L1"],
    "Colegio de Ingenieros": ["L1"],
    "Plaza Venezuela": ["L1", "L3"],  # Transferencia L1/L3
    "Sabana Grande": ["L1"],
    "Chacaíto": ["L1"],
    "Chacao": ["L1"],
    "Altamira": ["L1"],
    "Miranda": ["L1"],
    "Los Dos Caminos": ["L1"],
    "Los Cortijos": ["L1"],
    "La California": ["L1"],
    "Petare": ["L1"],
    "Palo Verde": ["L1"],

    # Línea 2
    "El Silencio": ["L2"],
    "Maternidad": ["L2"],
    "Artigas": ["L2"],
    "La Paz": ["L2"],
    "La Yaguara": ["L2"],
    "Carapita": ["L2"],
    "Antímano": ["L2"],
    "Mamera": ["L2"],
    "Ruiz Pineda": ["L2"],
    "Las Adjuntas": ["L2"],
    "Caricuao": ["L2"],
    "Zoológico": ["L2"],

    # Línea 3
    "Plaza Venezuela": ["L1", "L3"],
    "Ciudad Universitaria": ["L3"],
    "Los Símbolos": ["L3"],
    "La Bandera": ["L3"],
    "El Valle": ["L3"],
    "Los Jardines": ["L3"],
    "Coche": ["L3"],
    "Mercado": ["L3"],
    "La Rinconada": ["L3"],

    # Línea 4 / Línea 5
    "Zona Rental": ["L4", "L5"],
    "Parque Central": ["L4"],
    "Nuevo Circo": ["L4"],
    "Teatros": ["L4"],
    "Capuchinos": ["L2", "L4"],  # Transferencia L2/L4
    "Bello Monte": ["L5"]
}

# Diccionario de Adyacencia (Grafo con pesos en minutos)
GRAFO_METRO = {
    # --- LÍNEA 1 ---
    "Propatria": [("Pérez Bonalde", 2)],
    "Pérez Bonalde": [("Propatria", 2), ("Plaza Sucre", 2)],
    "Plaza Sucre": [("Pérez Bonalde", 2), ("Gato Negro", 2)],
    "Gato Negro": [("Plaza Sucre", 2), ("Agua Salud", 2)],
    "Agua Salud": [("Gato Negro", 2), ("Caño Amarillo", 2)],
    "Caño Amarillo": [("Agua Salud", 2), ("Capitolio", 2)],
    "Capitolio": [("Caño Amarillo", 2), ("La Hoyada", 2)],
    "La Hoyada": [("Capitolio", 2), ("Parque Carabobo", 2)],
    "Parque Carabobo": [("La Hoyada", 2), ("Bellas Artes", 2)],
    "Bellas Artes": [("Parque Carabobo", 2), ("Colegio de Ingenieros", 2)],
    "Colegio de Ingenieros": [("Bellas Artes", 2), ("Plaza Venezuela", 2)],
    "Plaza Venezuela": [
        ("Colegio de Ingenieros", 2),
        ("Sabana Grande", 2),
        ("Ciudad Universitaria", 3),  # Conexión L3
        ("Zona Rental", 4)            # Pasillo de transferencia L4/L5
    ],
    "Sabana Grande": [("Plaza Venezuela", 2), ("Chacaíto", 2)],
    "Chacaíto": [("Sabana Grande", 2), ("Chacao", 2)],
    "Chacao": [("Chacaíto", 2), ("Altamira", 2)],
    "Altamira": [("Chacao", 2), ("Miranda", 2)],
    "Miranda": [("Altamira", 2), ("Los Dos Caminos", 2)],
    "Los Dos Caminos": [("Miranda", 2), ("Los Cortijos", 2)],
    "Los Cortijos": [("Los Dos Caminos", 2), ("La California", 2)],
    "La California": [("Los Cortijos", 2), ("Petare", 2)],
    "Petare": [("La California", 2), ("Palo Verde", 2)],
    "Palo Verde": [("Petare", 2)],

    # --- LÍNEA 4 ---
    "Zona Rental": [
        ("Plaza Venezuela", 4),       # Pasillo de transferencia L1/L3
        ("Parque Central", 2),
        ("Bello Monte", 3)            # Tramo L5
    ],
    "Parque Central": [("Zona Rental", 2), ("Nuevo Circo", 2)],
    "Nuevo Circo": [("Parque Central", 2), ("Teatros", 2)],
    "Teatros": [("Nuevo Circo", 2), ("Capuchinos", 2)],
    "Capuchinos": [
        ("Teatros", 2),
        ("El Silencio", 3),
        ("Maternidad", 2)             # Empalme hacia Línea 2
    ],

    # --- LÍNEA 2 ---
    "El Silencio": [("Capuchinos", 3)],
    "Maternidad": [("Capuchinos", 2), ("Artigas", 2)],
    "Artigas": [("Maternidad", 2), ("La Paz", 2)],
    "La Paz": [("Artigas", 2), ("La Yaguara", 2)],
    "La Yaguara": [("La Paz", 2), ("Carapita", 2)],
    "Carapita": [("La Yaguara", 2), ("Antímano", 2)],
    "Antímano": [("Carapita", 2), ("Mamera", 2)],
    "Mamera": [
        ("Antímano", 2),
        ("Ruiz Pineda", 3),
        ("Caricuao", 3)
    ],
    "Ruiz Pineda": [("Mamera", 3), ("Las Adjuntas", 3)],
    "Las Adjuntas": [("Ruiz Pineda", 3)],
    "Caricuao": [("Mamera", 3), ("Zoológico", 2)],
    "Zoológico": [("Caricuao", 2)],

    # --- LÍNEA 3 ---
    "Ciudad Universitaria": [("Plaza Venezuela", 3), ("Los Símbolos", 2)],
    "Los Símbolos": [("Ciudad Universitaria", 2), ("La Bandera", 2)],
    "La Bandera": [("Los Símbolos", 2), ("El Valle", 2)],
    "El Valle": [("La Bandera", 2), ("Los Jardines", 2)],
    "Los Jardines": [("El Valle", 2), ("Coche", 2)],
    "Coche": [("Los Jardines", 2), ("Mercado", 2)],
    "Mercado": [("Coche", 2), ("La Rinconada", 3)],
    "La Rinconada": [("Mercado", 3)],

    # --- LÍNEA 5 ---
    "Bello Monte": [("Zona Rental", 3)]
}


def obtener_lineas_de_estacion(estacion: str) -> list:
    """Devuelve la lista de líneas a las que pertenece una estación."""
    return LINEAS_ESTACION.get(estacion, [])


def obtener_estaciones_de_linea(linea: str) -> list:
    """Devuelve todas las estaciones que pertenecen a una línea específica (ej. 'L1')."""
    linea_up = linea.upper()
    return [
        estacion for estacion, lineas in LINEAS_ESTACION.items()
        if linea_up in lineas
    ]


def obtener_vecinos(estacion: str) -> list:
    """Devuelve las estaciones adyacentes y el tiempo de viaje hacia cada una."""
    return GRAFO_METRO.get(estacion, [])


def existe_estacion(estacion: str) -> bool:
    """Valida si una estación existe en la base de datos."""
    return estacion in GRAFO_METRO