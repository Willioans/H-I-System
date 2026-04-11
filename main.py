"""
🚀 H&I SYSTEM - VERSION 1.0
Sistema Multinegocios
"""

# Importamos todos los paneles que vamos a crear
from paneles.bodega import iniciar as iniciar_bodega
from paneles.tienda import iniciar as iniciar_tienda
from paneles.ferreteria import iniciar as iniciar_ferreteria
from paneles.gimnasio import iniciar as iniciar_gimnasio
from paneles.repuestos_moto import iniciar as iniciar_moto
from paneles.repuestos_carro import iniciar as iniciar_carro
from paneles.restaurante import iniciar as iniciar_restaurante

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
    elif opcion == "2":
        iniciar_tienda()
    elif opcion == "3":
        iniciar_ferreteria()
    elif opcion == "4":
        iniciar_gimnasio()
    elif opcion == "5":
        iniciar_moto()
    elif opcion == "6":
        iniciar_carro()
    elif opcion == "7":
        iniciar_restaurante()
    elif opcion == "0":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción no disponible todavía o incorrecta.")
    
    input("\nPresiona Enter para continuar...")
