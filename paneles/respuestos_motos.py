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
    cursor.execute("INSERT INTO repuestos_moto (codigo, nombre, modelo, precio) VALUES (?,?,?,?)",
                   (cod, nom, mod, prec))
    conn.commit()
    print(f"✅ Guardado! {formato_precio(prec)}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("    REPUESTOS DE MOTOCICLETA     ")
        print("==================================")
        print("1. ➕ Agregar Pieza")
        print("2. 🔍 Buscar por Modelo")
        print("3. 🚪 Salir")
        
        op = input("Opción: ")
        if op == "1": agregar_pieza()
        elif op == "3": break
        input("\nEnter...")
