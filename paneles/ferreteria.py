"""
🔩 PANEL DE FERRETERÍA
Sistema H&I
Materiales, Herramientas y Construcción
"""

def iniciar():
    print("==================================")
    print("     SISTEMA DE FERRETERÍA       ")
    print("==================================")
    print("🔨 PRODUCTOS:")
    print("1. Agregar Material")
    print("2. Control de Unidades (Kg, Mt, Lt)")
    print("3. Cotización Rápida")
    print("")
    print("📊 REPORTES:")
    print("4. Inventario Total")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("📝 Nuevo material...")
    elif opcion == "2":
        print("⚖️ Gestión de medidas...")
    elif opcion == "3":
        print("🧾 Generando cotización...")
    else:
        print("👋 Volviendo al menú...")
