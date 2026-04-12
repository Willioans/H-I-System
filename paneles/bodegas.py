"""
📦 PANEL DE BODEGA
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def ingresar_mercancia():
    print("\n📝 REGISTRAR NUEVO PRODUCTO")
    print("----------------------------")
    
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    cantidad = int(input("Cantidad: "))
    ubicacion = input("Ubicación: ")
    vencimiento = input("Vencimiento: ")
    costo = float(input("Costo: "))

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO productos_bodega (codigo, nombre, cantidad, ubicacion, fecha_vencimiento, costo)
            VALUES (?,?,?,?,?,?)
        ''', (codigo, nombre, cantidad, ubicacion, vencimiento, costo))
        conn.commit()
        print(f"✅ Guardado! Costo: {formato_precio(costo)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    conn.close()

def ver_inventario():
    print("\n📋 INVENTARIO GENERAL")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, cantidad, ubicacion, costo FROM productos_bodega")
    for p in cursor.fetchall():
        print(f"{p[0]} | Stock: {p[1]} | Ubic: {p[2]} | Valor: {formato_precio(p[3])}")
    conn.close()

def iniciar():
    while True:
        print("\n")
        print("==================================")
        print("        SISTEMA DE BODEGA         ")
        print("==================================")
        print("1. ➕ Ingresar Mercancía")
        print("2. 📋 Ver Inventario")
        print("6. 📊 Cargar desde Excel")
        print("3. 🚪 Salir")
        
        op = input("\nOpción: ")
        
        if op == "1":
            ingresar_mercancia()
        elif op == "2":
            ver_inventario()
        elif op == "6":
            from excel_manager import menu_importar
            menu_importar("bodega")
        elif op == "3":
            break
        else:
            print("❌ Opción no válida")
            
        input("\nPresiona Enter para continuar...")
