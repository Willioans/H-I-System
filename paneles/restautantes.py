"""
🍽️ RESTAURANTE
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def agregar_plato():
    print("\n🍔 NUEVO PLATO")
    nom = input("Nombre del Plato: ")
    cat = input("Categoría: ")
    prec = float(input("Precio: "))

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO menu (nombre, categoria, precio)
            VALUES (?,?,?)
        ''', (nom, cat, prec))
        conn.commit()
        print(f"✅ Agregado! Precio: {formato_precio(prec)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    conn.close()

def ver_menu():
    print("\n📋 MENÚ COMPLETO")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, categoria, precio FROM menu")
    for p in cursor.fetchall():
        print(f"{p[0]} ({p[1]}) - {formato_precio(p[2])}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("     SISTEMA DE RESTAURANTE      ")
        print("==================================")
        print("1. ➕ Agregar Plato al Menú")
        print("2. 📋 Ver Menú")
        print("6. 📊 Cargar desde Excel")
        print("3. 🚪 Salir")
        
        op = input("\nOpción: ")
        
        if op == "1":
            agregar_plato()
        elif op == "2":
            ver_menu()
        elif op == "6":
            from excel_manager import menu_importar
            menu_importar("restaurante")
        elif op == "3":
            break
        else:
            print("❌ Opción no válida")
            
        input("\nPresiona Enter para continuar...")
