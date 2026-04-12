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
    cursor.execute("INSERT INTO ferreteria (codigo, nombre, unidad, precio, stock) VALUES (?,?,?,?,?)",
                   (cod, nom, uni, prec, stk))
    conn.commit()
    print(f"✅ Agregado! {formato_precio(prec)}")
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
        print("3. 🧾 Cotización")
        print("4. 🚪 Salir")
        
        op = input("Opción: ")
        if op == "1": agregar_material()
        elif op == "2": ver_listado()
        elif op == "4": break
        input("\nEnter...")
