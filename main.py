"""
🚀 H&I SYSTEM - VERSION 1.0
Sistema Multinegocios
© Copyright 2025
"""

# ===== IMPORTACIONES GENERALES =====
from base_datos import inicializar_db
from auth import pantalla_login, crear_admin_default
from paneles.bodega import iniciar as iniciar_bodega
from paneles.tienda import iniciar as iniciar_tienda
from paneles.ferreteria import iniciar as iniciar_ferreteria
from paneles.gimnasio import iniciar as iniciar_gimnasio
from paneles.repuestos_moto import iniciar as iniciar_moto
from paneles.repuestos_carro import iniciar as iniciar_carro
from paneles.restaurante import iniciar as iniciar_restaurante
from admin_panel import iniciar_admin  # 👑 NUEVO: PANEL DE ADMIN

# ===== MENÚ PRINCIPAL =====
def menu_principal():
    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║          H&I SYSTEM - MASTER         ║")
    print("╚══════════════════════════════════════╝")
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
    print("👑 [9] PANEL DE ADMINISTRACIÓN 🔒")
    print("🚪 [0] SALIR DEL SISTEMA")
    print("----------------------------------")

# ===== PROGRAMA PRINCIPAL =====
def main():
    # 1. INICIAR SISTEMA Y BASE DE DATOS
    print("🚀 INICIANDO H&I SYSTEM...")
    crear_admin_default()
    inicializar_db()

    # 2. PANTALLA DE LOGIN
    usuario_actual = None
    while not usuario_actual:
        usuario_actual = pantalla_login()

    # 3. BUCLE DEL MENÚ PRINCIPAL
    while True:
        menu_principal()
        opcion = input("👉 Digite el número del sistema: ")

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
        elif opcion == "9":
            iniciar_admin()  # ✅ AQUÍ LLAMA AL PANEL DE ADMIN
        elif opcion == "0":
            print("👋 Saliendo del sistema... Hasta luego!")
            break
        else:
            print("❌ Opción no disponible o incorrecta.")
        
        input("\nPresiona Enter para continuar...")

# EJECUTAR PROGRAMA
if __name__ == "__main__":
    main()
