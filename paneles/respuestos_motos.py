"""
🏍️ REPUESTOS MOTO
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def agregar_pieza():
    print("\n🔧 NUEVA PIEZA")
    cod = input("Código OEM: ")
    nom = input("Nombre: ")
    mod = input("Modelo compatible: ")
    prec = float(input("Precio: "))

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO repuestos_moto (codigo, nombre, modelo, precio)
            VALUES (?,?,?,?)
        ''', (cod, nom, mod, prec))
        conn.commit()
        print(f"✅ Guardado! Precio: {formato_precio(prec)}")
    except Exception as e:
        print(f"❌ Error: {e}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("    REPUESTOS DE MOTOCICLETA     ")
        print("==================================")
        print("1. ➕ Agregar Pieza")
        print("2. 🔍 Buscar por Modelo")
        print("6. 📊 Cargar desde Excel")
        print("3. 🚪 Salir")
        
        op = input("\nOpción: ")
        
        if op == "1":
            agregar_pieza()
        elif op == "6":
            from excel_manager import menu_importar
            menu_importar("moto")
        elif op == "3":
            break
        else:
            print("❌ Opción no válida")
            
        input("\nPresiona Enter para continuar...")
