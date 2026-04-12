"""
📦 PANEL DE BODEGA
Sistema H&I
"""

import sys
import os

# Agregamos esto para que pueda importar la base de datos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar

def ingresar_mercancia():
    print("\n📝 REGISTRAR NUEVO PRODUCTO")
    print("----------------------------")
    
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    ubicacion = input("Ubicación (Pasillo/Estante): ")
    vencimiento = input("Fecha de vencimiento (opcional): ")

    # Conectar y guardar
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO productos_bodega (codigo, nombre, cantidad, ubicacion, fecha_vencimiento)
            VALUES (?, ?, ?, ?, ?)
        ''', (codigo, nombre, cantidad, ubicacion, vencimiento))
        
        conn.commit()
        print(f"✅ Producto '{nombre}' guardado correctamente!")
    except Exception as e:
        print(f"❌ Error: El código ya existe o hubo un problema. Detalle: {e}")
    
    conn.close()

def ver_inventario():
    print("\n📋 LISTA DE INVENTARIO")
    print("-----------------------")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos_bodega")
    productos = cursor.fetchall()
    
    if not productos:
        print("⚠️ No hay productos registrados aún.")
    else:
        for p in productos:
            print(f"ID: {p[0]} | Código: {p[1]} | Nombre: {p[2]} | Cant: {p[3]} | Ubic: {p[4]}")
    
    conn.close()

def iniciar():
    while True:
        print("\n")
        print("==================================")
        print("        SISTEMA DE BODEGA         ")
        print("==================================")
        print("1. ➕ Ingresar Mercancía")
        print("2. 📋 Ver Inventario")
        print("3. 🚪 Salir al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            ingresar_mercancia()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción incorrecta, intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")
