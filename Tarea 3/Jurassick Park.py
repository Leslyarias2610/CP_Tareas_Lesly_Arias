import unicodedata

# ==========================================
# BASE DE DATOS DE DINOSAURIOS DE JURASSIC PARK
# ==========================================

base_de_datos_dinosaurios = [
    ("Tyrannosaurus Rex", "Rex", "Carnívoro", "Cretácico"),
    ("Velociraptor", "Antirrhopus", "Carnívoro", "Cretácico"),
    ("Triceratops", "Prorsus", "Herbívoro", "Cretácico"),
    ("Brachiosaurus", "Altithorax", "Herbívoro", "Jurásico"),
    ("Spinosaurus", "Aegyptiacus", "Carnívoro", "Cretácico"),
    ("Stegosaurus", "Armatus", "Herbívoro", "Jurásico")
]


# ==========================================
# FUNCIÓN AUXILIAR DE NORMALIZACIÓN
# ==========================================

def normalizar_texto(texto):
    """Convierte el texto a minúsculas y elimina tildes/acentos."""
    if not texto:
        return ""
    # Normaliza caracteres Unicode separando las tildes de las letras base
    nfkd_form = unicodedata.normalize('NFKD', texto)
    # Filtra los caracteres que no sean marcas diacríticas (tildes) y los pasa a minúscula
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()


# ==========================================
# FUNCIONES DE BÚSQUEDA Y FLUJO INTERACTIVO
# ==========================================

def informacion_dinosaurio(base_de_datos):
    """Busca dinosaurios por nombre parcial (ignorando tildes y mayúsculas) y pide confirmación."""
    while True:
        print("\n" + "─" * 47)
        entrada = input("🔹 Ingresa el nombre o parte del nombre (ej. 'rex', 'raptor') o 'volver': ").strip()
        
        if entrada.lower() == 'volver':
            break
            
        buscado_norm = normalizar_texto(entrada)
        encontrados = [dino for dino in base_de_datos if buscado_norm in normalizar_texto(dino[0])]
        
        if not encontrados:
            print(f"\n⚠️ [Aviso]: No se encontraron dinosaurios que coincidan con '{entrada}'.")
            continue

        encontro_uno = False
        for dino in encontrados:
            nombre_completo = dino[0]
            print("\n" + "─" * 47)
            confirmacion = input(f"🔹 ¿Quisiste decir '{nombre_completo}'? (s/n): ").strip().lower()
            
            if confirmacion == 's':
                print("\n" + "┌" + "─" * 53 + "┐")
                print(f"│ 🦖 Nombre: {dino[0]}".ljust(54) + "│")
                print(f"│ 🧬 Especie: {dino[1]}".ljust(54) + "│")
                print(f"│ 🥩 Dieta:   {dino[2]}".ljust(54) + "│")
                print(f"│ ⏳ Período: {dino[3]}".ljust(54) + "│")
                print("└" + "─" * 53 + "┘")
                encontro_uno = True
                break
                
        if not encontro_uno and len(encontrados) > 0:
            print("\nℹ️ [Aviso]: Búsqueda finalizada sin confirmación de registros.")
            
        print("\n" + "─" * 47)
        otra = input("🔄 ¿Deseas realizar otra búsqueda por nombre? (s/n): ").strip().lower()
        if otra != 's':
            break


def dinosaurios_por_dieta(base_de_datos):
    """Busca dietas por coincidencia parcial, pide confirmación interactiva y muestra resultados."""
    # Extraer las dietas únicas disponibles de la base de datos
    dietas_unicas = sorted(list(set(dino[2] for dino in base_de_datos)))
    
    while True:
        print("\n" + "─" * 47)
        entrada = input("🔹 Ingresa la dieta o parte de ella (ej. 'carn', 'herbi') o 'volver': ").strip()
        
        if entrada.lower() == 'volver':
            break
            
        buscado_norm = normalizar_texto(entrada)
        
        # Encontrar dietas únicas que coincidan parcialmente con lo ingresado
        dietas_coincidentes = [d for d in dietas_unicas if buscado_norm in normalizar_texto(d)]
        
        if not dietas_coincidentes:
            print(f"\n⚠️ [Aviso]: No se encontraron dietas que coincidan con '{entrada}'.")
            continue

        encontro_una_dieta = False
        for dieta_completa in dietas_coincidentes:
            print("\n" + "─" * 47)
            confirmacion = input(f"🔹 ¿Quisiste decir '{dieta_completa}'? (s/n): ").strip().lower()
            
            if confirmacion == 's':
                encontro_una_dieta = True
                # Filtrar todos los dinosaurios que tengan esta dieta exacta
                resultados = [dino for dino in base_de_datos if normalizar_texto(dino[2]) == normalizar_texto(dieta_completa)]
                
                print(f"\n╔" + "═" * 55 + "╗")
                print(f"║ 🥩 DINOSAURIOS CON DIETA: {dieta_completa.upper()} ".center(55) + "║")
                print(f"╚" + "═" * 55 + "╝")
                for dino in resultados:
                    print(f" • 🦖 {dino[0]} (Especie: {dino[1]} | Período: {dino[3]})")
                break
                
        if not encontro_una_dieta:
            print("\nℹ️ [Aviso]: Búsqueda de dieta finalizada sin confirmación.")
            
        print("\n" + "─" * 47)
        otra = input("🔄 ¿Deseas consultar otra dieta? (s/n): ").strip().lower()
        if otra != 's':
            break


def dinosaurios_por_periodo(base_de_datos):
    """Muestra los períodos geológicos disponibles y permite seleccionarlos por número."""
    periodos_unicos = sorted(list(set(dino[3] for dino in base_de_datos)))
    
    while True:
        print("\n" + "╔" + "═" * 45 + "╗")
        print("║" + " ⏳ SELECCIONA UN PERÍODO GEOLÓGICO ⏳ ".center(45) + "║")
        print("╚" + "═" * 45 + "╝")
        
        for idx, periodo in enumerate(periodos_unicos, 1):
            print(f" [{idx}] ⏳ {periodo}")
        print(" [v] ↩️ Volver al menú principal")
        print("─" * 47)
        
        seleccion = input("🔹 Selecciona el número de tu opción: ").strip().lower()
        
        if seleccion == 'v':
            break
            
        try:
            indice = int(seleccion) - 1
            if 0 <= indice < len(periodos_unicos):
                periodo_seleccionado = periodos_unicos[indice]
                
                resultados = [dino for dino in base_de_datos if normalizar_texto(dino[3]) == normalizar_texto(periodo_seleccionado)]
                
                print(f"\n╔" + "═" * 55 + "╗")
                print(f"║ ⏳ DINOSAURIOS DEL PERÍODO: {periodo_seleccionado.upper()} ".center(55) + "║")
                print(f"╚" + "═" * 55 + "╝")
                for dino in resultados:
                    print(f" • 🦖 {dino[0]} (Especie: {dino[1]} | Dieta: {dino[2]})")
                    
                print("\n" + "─" * 47)
                input("🔹 Presiona [Enter] para continuar... ")
            else:
                print("\n⚠️ [Error]: Número fuera de rango. Por favor selecciona una opción válida.")
        except ValueError:
            print("\n⚠️ [Error]: Debes ingresar un número válido o 'v' para volver.")


def mostrar_todos(base_de_datos):
    """Muestra la lista completa del parque y hace una pausa para que el usuario lea."""
    print(f"\n╔" + "═" * 55 + "╗")
    print(f"║ 📋 REGISTRO GENERAL DE JURASSIC PARK 📋 ".center(55) + "║")
    print(f"╚" + "═" * 55 + "╝")
    for idx, dino in enumerate(base_de_datos, 1):
        print(f" {idx}. **{dino[0]}** | Especie: {dino[1]} | Dieta: {dino[2]} | Período: {dino[3]}")
    
    print("\n" + "─" * 47)
    input("🔹 Presiona [Enter] para regresar al menú principal... ")


# ==========================================
# INTERFAZ DE USUARIO (MENÚ PRINCIPAL)
# ==========================================

def menu_principal():
    print("╔" + "═" * 55 + "╗")
    print("║" + " 🌴 SISTEMA INTELIGENTE DE JURASSIC PARK 🌴 ".center(55) + "║")
    print("╚" + "═" * 55 + "╝")
    
    while True:
        print("\n" + "─" * 57)
        print(" [1] 🔍 Buscar dinosaurio por Nombre (con confirmación y sin tildes)")
        print(" [2] 🥩 Buscar dinosaurios por Dieta (parcial con confirmación)")
        print(" [3] ⏳ Buscar dinosaurios por Período (Selección numérica)")
        print(" [4] 📋 Ver todos los registros del parque")
        print(" [5] 🚪 Salir del sistema")
        print("─" * 57)
        
        opcion = input("🔹 Selecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            informacion_dinosaurio(base_de_datos_dinosaurios)
            
        elif opcion == '2':
            dinosaurios_por_dieta(base_de_datos_dinosaurios)
            
        elif opcion == '3':
            dinosaurios_por_periodo(base_de_datos_dinosaurios)
            
        elif opcion == '4':
            mostrar_todos(base_de_datos_dinosaurios)
            
        elif opcion == '5':
            print("\n✨ ¡Cerrando sistemas de Jurassic Park. Que tengas un excelente día! 🦖✨\n")
            break
        else:
            print("\n⚠️ [Error]: Opción no válida. Por favor selecciona un número del 1 al 5.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    menu_principal()