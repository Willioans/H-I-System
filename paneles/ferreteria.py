"""
🔩 PANEL DE FERRETERÍA
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def agregar_material():
    print("\n🔨 NUEVO MATERIAL")
    cod = input("Código: ")
    nom = input("Nombre: ")
    uni = input("Unidad (Mts, Kg, Pza): ")
    prec = float(input("Precio: "))
    stk = int(input("Stock: "))

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO ferreteria (codigo, nombre, unidad, precio, stock)
            VALUES (?,?,?,?,?)
        ''', (cod, nom, uni, prec, stk))
        conn.commit()
        print(f"✅ Agregado! Precio: {formato_precio(prec)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    conn.close()

def ver_listado():
    print("\n📋 LISTA DE MATERIALES")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, unidad, precio, stock FROM ferreteria")
    for p in cursor.fetchall():
        print(f"{p[0]} | {p[1]} | Precio: {formato_precio(p[2])} | Stock: {p[3]}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("     SISTEMA DE FERRETERÍA       ")
        print("==================================")
        print("1. ➕ Agregar Material")
        print("2. 📋 Ver Inventario")
        print("6. 📊 Cargar desde Excel")
        print("3. 🚪 Salir")
        
        op = input("\nOpción: ")
        
        if op == "1":
            agregar_material()
        elif op == "2":
            ver_listado()
        elif op == "6":
            from excel_manager import menu_importar
            menu_importar("ferreteria")
        elif op == "3":
            break
        else:
            print("❌ Opción no válida")
            
        input("\nPresiona Enter para continuar...")
