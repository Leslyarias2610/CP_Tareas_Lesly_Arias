import pandas as pd

def procesar_cambios_escena(escena, salud, hambre):
    """Aplica las variaciones de salud y hambre indicadas en la escena actual."""
    nueva_salud = salud
    nuevo_hambre = hambre

    if pd.notna(escena.get("cambio_salud")):
        nueva_salud = max(0, min(100, salud + int(escena["cambio_salud"])))
    
    if pd.notna(escena.get("cambio_hambre")):
        nuevo_hambre = max(0, min(100, hambre + int(escena["cambio_hambre"])))

    return nueva_salud, nuevo_hambre

def agregar_objeto(escena, inventario):
    """Verifica si la escena otorga un objeto y lo añade al inventario sin duplicarlo."""
    objeto = escena.get("otorga_objeto")
    if pd.notna(objeto) and str(objeto).strip() != "":
        obj_clean = str(objeto).strip().lower()
        if obj_clean not in inventario:
            inventario.append(obj_clean)
            print(f"\n✨ ¡Objeto obtenido: '{obj_clean.upper()}'!")

def validar_objeto_requerido(escena, inventario):
    """Comprueba si la escena exige un objeto del inventario para poder continuar."""
    requiere = escena.get("requiere_objeto")
    if pd.notna(requiere) and str(requiere).strip() != "":
        obj_req = str(requiere).strip().lower()
        if obj_req not in inventario:
            return False, obj_req
    return True, None