"""
🚗 PANEL REPUESTOS DE CARRO
Sistema H&I
Sistema Avanzado
"""

def iniciar():
    print("==================================")
    print("      REPUESTOS DE AUTOS         ")
    print("==================================")
    print("🚗 VEHÍCULO:")
    print("1. Seleccionar Marca / Modelo")
    print("2. Por Motor / Chasis")
    print("")
    print("📋 CATÁLOGO:")
    print("3. Originales vs Alternativos")
    print("4. Lista de Piezas")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("🚙 Selección de vehículo...")
    elif opcion == "2":
        print("🔧 Especificaciones de motor...")
    else:
        print("👋 Volviendo al menú...")
