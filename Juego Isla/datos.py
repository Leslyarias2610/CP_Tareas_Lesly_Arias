import pandas as pd
from datetime import datetime

def cargar_escenas(ruta_archivo="escenas_isla.xlsx"):
    """Carga la tabla de escenas desde el archivo Excel."""
    try:
        df = pd.read_excel(ruta_archivo)
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        return None

def buscar_escena(df, id_escena):
    """Busca una escena específica por su id_escena y devuelve una Serie."""
    filtro = df[df["id_escena"] == id_escena]
    if filtro.empty:
        return None
    return filtro.squeeze()

def guardar_estado_partida(escena_actual, inventario, dia, salud, hambre, tipo_final):
    """Exporta el resumen de la partida a estado_partida.xlsx usando Pandas."""
    inventario_texto = ", ".join(inventario) if inventario else "sin objetos"
    
    estado = {
        "escena_final": escena_actual,
        "dias_sobrevividos": dia,
        "salud_final": salud,
        "hambre_final": hambre,
        "inventario": inventario_texto,
        "tipo_final": tipo_final,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    df_estado = pd.DataFrame([estado])
    df_estado.to_excel("estado_partida.xlsx", index=False)
    print("\n💾 Partida guardada exitosamente en 'estado_partida.xlsx'.")