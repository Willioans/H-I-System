"""
💪 PANEL DE GIMNASIO
Sistema H&I
Control de Membresías y Acceso
"""

def iniciar():
    print("==================================")
    print("      SISTEMA DE GIMNASIO        ")
    print("==================================")
    print("🧍 MIEMBROS:")
    print("1. Registrar Nuevo Socio")
    print("2. Control de Membresías")
    print("3. Ver Vencimientos")
    print("")
    print("🚪 ACCESO:")
    print("4. Registrar Entrada/Salida")
    print("")
    print("🚪 0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        print("📝 Datos del nuevo miembro...")
    elif opcion == "2":
        print("💳 Planes y pagos...")
    elif opcion == "3":
        print("⚠️ Lista de membresías por vencer...")
    else:
        print("👋 Volviendo al menú...")
 
