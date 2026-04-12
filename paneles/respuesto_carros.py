"""
🚗 REPUESTOS CARRO
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def agregar_pieza():
    print("\n🚗 NUEVA PIEZA")
    cod = input("Código: ")
    nom = input("Nombre: ")
    motor = input("Tipo de Motor: ")
    prec = float(input("Precio: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO repuestos_carro (codigo, nombre, motor, precio) VALUES (?,?,?,?)",
                   (cod, nom, motor, prec))
    conn.commit()
    print(f"✅ Guardado! {formato_precio(prec)}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("      REPUESTOS DE AUTOS         ")
        print("==================================")
        print("1. ➕ Agregar Pieza")
        print("2. 📋 Catálogo Completo")
        print("3. 🚪 Salir")
        
        op = input("Opción: ")
        if op == "1": agregar_pieza()
        elif op == "3": break
        input("\nEnter...")
