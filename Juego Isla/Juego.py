from datos import cargar_escenas, buscar_escena, guardar_estado_partida
from mecanicas import procesar_cambios_escena, agregar_objeto, validar_objeto_requerido
import pandas as pd

def iniciar_juego():
    df_escenas = cargar_escenas("escenas_isla.xlsx")
    if df_escenas is None:
        return

    # Estado inicial del jugador
    escena_actual = "inicio"
    inventario = []
    salud = 100
    hambre = 0
    dia = 1
    juego_activo = True

    print("==================================================")
    print(" 🌴 AVENTURA EN LA ISLA PERDIDA: SUPERVIVENCIA 🌴")
    print("==================================================\n")

    while juego_activo:
        escena = buscar_escena(df_escenas, escena_actual)
        
        if escena is None:
            print(f"\n❌ Error: La escena '{escena_actual}' no existe en el Excel.")
            break

        # Actualizar indicadores
        salud, hambre = procesar_cambios_escena(escena, salud, hambre)

        # Penalización por hambre
        if hambre >= 100:
            salud -= 15
            print("\n⚠️ ¡Tienes demasiado hambre! Perdiste -15 HP.")

        # Condición de derrota
        if salud <= 0:
            print("\n💀 Te has quedado sin salud. No lograste sobrevivir.")
            guardar_estado_partida(escena_actual, inventario, dia, salud, hambre, "malo_muerte")
            break

        # Condición de victoria
        if dia >= 7:
            print("\n🎉 ¡HAS SOBREVIVIDO 7 DÍAS! Un barco te ha rescatado.")
            guardar_estado_partida(escena_actual, inventario, dia, salud, hambre, "victoria_7dias")
            break

        # Mostrar interfaz
        print("-" * 50)
        print(f"📅 DÍA {dia} | ❤️ Salud: {salud}% | 🍖 Hambre: {hambre}%")
        print(f"📍 UBICACIÓN: {escena_actual.upper()}")
        print(f"📖 {escena['descripcion']}\n")

        # Otorgar objetos
        agregar_objeto(escena, inventario)
        print(f"🎒 Inventario: {inventario if inventario else 'Vacío'}")

        # Evaluar final de escena
        es_final = bool(escena.get("es_final")) if pd.notna(escena.get("es_final")) else False
        if es_final:
            mensaje = escena.get("mensaje_final")
            tipo_final = escena.get("tipo_final")
            print(f"\n🏁 {mensaje if pd.notna(mensaje) else 'Fin del juego.'}")
            guardar_estado_partida(escena_actual, inventario, dia, salud, hambre, tipo_final)
            break

        # Opciones de juego
        print("\nOpciones de acción:")
        print(f" [A] {escena['opcion_a']}")
        print(f" [B] {escena['opcion_b']}")
        if "fruta" in inventario or "pescado" in inventario:
            print(" [C] Comer del inventario (-30% Hambre)")

        opcion = input("\n👉 Selecciona una opción (A/B/C): ").strip().upper()

        if opcion == "A":
            tiene_objeto, obj_req = validar_objeto_requerido(escena, inventario)
            if not tiene_objeto:
                print(f"\n❌ Necesitas tener '{obj_req.upper()}' para tomar esta ruta.")
            else:
                escena_actual = str(escena["destino_a"]).strip()
                dia += 0.5
        elif opcion == "B":
            escena_actual = str(escena["destino_b"]).strip()
            dia += 0.5
        elif opcion == "C" and ("fruta" in inventario or "pescado" in inventario):
            if "fruta" in inventario:
                inventario.remove("fruta")
                print("\n🍎 Te comiste una fruta.")
            elif "pescado" in inventario:
                inventario.remove("pescado")
                print("\n🐟 Te comiste un pescado.")
            hambre = max(0, hambre - 30)
        else:
            print("\n❌ Opción no válida.")

if __name__ == "__main__":
    iniciar_juego()