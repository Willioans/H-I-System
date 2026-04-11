"""
🏍️ PANEL REPUESTOS DE MOTO
Sistema H&I
Catálogo Técnico
"""

def iniciar():
    print("==================================")
    print("    REPUESTOS DE MOTOCICLETA     ")
    print("==================================")
    print("🔧 BÚSQUEDA:")
    print("1. Por Marca / Modelo / Año")
    print("2. Por Código OEM / Referencia")
    print("")
    print("📦 PRODUCTOS:")
    print("3. Agregar Pieza")
    print("4. Control de Stock")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("🏍️ Filtrando por vehículo...")
    elif opcion == "2":
        print("🔍 Buscando referencia técnica...")
    else:
        print("👋 Volviendo al menú...")
