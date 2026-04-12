"""
👕 PANEL DE TIENDA
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def ingresar_producto():
    print("\n📝 NUEVO ARTÍCULO")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    talla = input("Talla: ")
    color = input("Color: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO productos_tienda (codigo, nombre, talla, color, precio, stock)
            VALUES (?,?,?,?,?,?)
        ''', (codigo, nombre, talla, color, precio, stock))
        conn.commit()
        print(f"✅ Guardado! Precio: {formato_precio(precio)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    conn.close()

def ver_productos():
    print("\n📋 CATÁLOGO")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, talla, color, precio, stock FROM productos_tienda")
    for p in cursor.fetchall():
        print(f"{p[0]} | Talla:{p[1]} | Color:{p[2]} | Precio:{formato_precio(p[3])}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("       SISTEMA DE TIENDA         ")
        print("==================================")
        print("1. ➕ Agregar Producto")
        print("2. 📋 Ver Catálogo")
        print("6. 📊 Cargar desde Excel")
        print("3. 🚪 Salir")
        
        op = input("\nOpción: ")
        
        if op == "1":
            ingresar_producto()
        elif op == "2":
            ver_productos()
        elif op == "6":
            from excel_manager import menu_importar
            menu_importar("tienda")
        elif op == "3":
            break
        else:
            print("❌ Opción no válida")
            
        input("\nPresiona Enter para continuar...")
