"""
🚀 H&I SYSTEM - VERSION 1.0
Sistema Multinegocios
"""

# Importamos los paneles que hemos creado
from paneles.bodega import iniciar as iniciar_bodega

def menu_principal():
    print("==================================")
    print("      H&I SYSTEM - MASTER        ")
    print("==================================")
    print("🔧 SELECCIONE SU MÓDULO:")
    print("")
    print("📦 [1] PANEL DE BODEGA")
    print("👕 [2] PANEL DE TIENDA")
    print("🔩 [3] PANEL DE FERRETERÍA")
    print("💪 [4] PANEL DE GIMNASIO")
    print("🏍️ [5] REPUESTOS DE MOTOS")
    print("🚗 [6] REPUESTOS DE CARROS")
    print("🍽️ [7] PANEL DE RESTAURANTE")
    print("")
    print("🚪 [0] SALIR")
    print("----------------------------------")

while True:
    menu_principal()
    opcion = input("Digite el número del sistema: ")

    if opcion == "1":
        iniciar_bodega()
    elif opcion == "0":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción no disponible todavía o incorrecta.")
        input("Presiona Enter para continuar...")
