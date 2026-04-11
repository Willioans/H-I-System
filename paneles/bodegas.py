"""
📦 PANEL DE BODEGA
Sistema H&I
"""

def iniciar():
    print("==================================")
    print("        SISTEMA DE BODEGA         ")
    print("==================================")
    print("1. Ingresar Mercancía")
    print("2. Ver Inventario")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("✅ Formulario de ingreso de productos...")
        # Aquí luego programamos el guardado
    elif opcion == "2":
        print("📋 Mostrando lista de productos...")
    else:
        print("👋 Saliendo...")
