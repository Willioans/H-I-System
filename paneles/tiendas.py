"""
👕 PANEL DE TIENDA
Sistema H&I
Especial para Ropa, Calzado y Accesorios
"""

def iniciar():
    print("==================================")
    print("       SISTEMA DE TIENDA         ")
    print("==================================")
    print("📦 PRODUCTOS:")
    print("1. Registrar Nuevo Artículo")
    print("2. Ver Catálogo")
    print("3. Buscar por Talla / Color")
    print("4. Actualizar Precio")
    print("")
    print("📊 REPORTES:")
    print("5. Productos más vendidos")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("📝 Abriendo formulario...")
        print("(Campos: Código, Nombre, Talla, Color, Precio, Stock)")
    elif opcion == "2":
        print("📋 Mostrando lista completa...")
    elif opcion == "3":
        print("🔍 Filtro por Talla y Color...")
    elif opcion == "4":
        print("💲 Modificador de precios...")
    else:
        print("👋 Volviendo al menú principal...")
