"""
💪 PANEL DE GIMNASIO
Sistema H&I
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_datos import conectar
from config import formato_precio

def registrar_socio():
    print("\n🧍 NUEVO SOCIO")
    nom = input("Nombre: ")
    tel = input("Teléfono: ")
    plan = input("Plan (Mensual/Anual): ")
    pago = float(input("Pago: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO socios (nombre, telefono, plan, pago) VALUES (?,?,?,?)",
                   (nom, tel, plan, pago))
    conn.commit()
    print(f"✅ Registrado! Pago: {formato_precio(pago)}")
    conn.close()

def iniciar():
    while True:
        print("\n==================================")
        print("      SISTEMA DE GIMNASIO        ")
        print("==================================")
        print("1. ➕ Registrar Socio")
        print("2. 📋 Ver Membresías")
        print("3. 🚪 Entrada/Salida")
        print("4. 🚪 Salir")
        
        op = input("Opción: ")
        if op == "1": registrar_socio()
        elif op == "4": break
        input("\nEnter...")
