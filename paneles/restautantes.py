"""
🍽️ PANEL DE RESTAURANTE
Sistema H&I
Pedidos y Menú QR
"""

def iniciar():
    print("==================================")
    print("     SISTEMA DE RESTAURANTE      ")
    print("==================================")
    print("📋 MESAS:")
    print("1. Ver Estado de Mesas")
    print("2. Tomar Pedido Manual")
    print("3. Pedidos por Código QR")
    print("")
    print("🍳 COCINA:")
    print("4. Ver Comandas Pendientes")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("🪑 Estado de mesas: Libre / Ocupada...")
    elif opcion == "3":
        print("📱 Generando menú digital QR...")
    elif opcion == "4":
        print("🔥 Pedidos listos para cocinar...")
    else:
        print("👋 Volviendo al menú...")
 
